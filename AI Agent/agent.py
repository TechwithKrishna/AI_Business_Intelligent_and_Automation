# agent.py

from utils.data import prepare_data
from NLP_Sentiment_Model.sentiment_model import load_model
from LLM_Recommendation_and_Insights.ai import generate_insights


def run_agent():

    # ---------------------------------
    # 1. Load combined Amazon data
    # ---------------------------------

    data = prepare_data()

    # ---------------------------------
    # 2. Load trained sentiment model
    # ---------------------------------

    sentiment_model = load_model()

    # ---------------------------------
    # 3. Predict sentiment
    # ---------------------------------

    reviews = data["review_text"].dropna().astype(str)

    sentiments = sentiment_model.predict(reviews)

    data.loc[reviews.index, "sentiment"] = sentiments

    # ---------------------------------
    # 4. Calculate statistics
    # ---------------------------------

    sentiment_counts = data["sentiment"].value_counts()

    positive = sentiment_counts.get("positive", 0)
    neutral = sentiment_counts.get("neutral", 0)
    negative = sentiment_counts.get("negative", 0)

    total_reviews = len(data)

    total_products = data["ProductId"].nunique()

    average_rating = data["Score"].mean()

    # ---------------------------------
    # 5. Product information
    # ---------------------------------

    if "monthly_sales" in data.columns:

        total_monthly_sales = pd.to_numeric(
            data["monthly_sales"],
            errors="coerce"
        ).sum()

    else:

        total_monthly_sales = 0

    # ---------------------------------
    # 6. Create summary for Gemini
    # ---------------------------------

    feedback_columns = [
        "ProductId",
        "product_name",
        "review_text",
        "Score",
        "sentiment"
    ]

    available_columns = [
        column
        for column in feedback_columns
        if column in data.columns
    ]

    feedback = (
        data[available_columns]
        .dropna()
        .head(50)
        .to_string(index=False)
    )

    summary = f"""
Amazon Business Intelligence Summary

Total Products:
{total_products}

Total Reviews:
{total_reviews}

Average Customer Rating:
{average_rating:.2f}

Monthly Sales:
{total_monthly_sales}

Customer Sentiment:

Positive: {positive}
Neutral: {neutral}
Negative: {negative}

Customer Feedback:

{feedback}
"""

    # ---------------------------------
    # 7. Send data to Gemini
    # ---------------------------------

    insights = generate_insights(summary)

    # ---------------------------------
    # 8. Return results
    # ---------------------------------

    return data, insights


# ---------------------------------
# Test Agent
# ---------------------------------

if __name__ == "__main__":

    data, insights = run_agent()

    print("\n")
    print("=" * 50)
    print("AI AGENT INSIGHTS")
    print("=" * 50)
    print("\n")

    print(insights)
