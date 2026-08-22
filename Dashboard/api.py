from fastapi import FastAPI
from pydantic import BaseModel

from utils.data import prepare_data
from NLP_Sentiment_Model.sentiment_model import (
    load_model,
    predict_sentiment
)

from LLM_Recommendation_and_Insights.ai import generate_insights
import pandas as pd


# =============================
# FastAPI App
# =============================

app = FastAPI(
    title="AI Business Intelligence API",
    description="Customer Feedback Intelligence and Business Analytics API",
    version="1.0.0"
)


# =============================
# Request Model
# =============================

class ReviewRequest(BaseModel):

    review: str


# =============================
# Home
# =============================

@app.get("/")
def home():

    return {
        "message": "AI Business Intelligence API is running"
    }


# =============================
# Health Check
# =============================

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# =============================
# Get Business Data
# =============================

@app.get("/data")
def get_data():

    data = prepare_data()

    result = (
        data
        .head(100)
        .fillna("")
        .to_dict(orient="records")
    )

    return {
        "total_rows": len(data),
        "data": result
    }


# =============================
# Sentiment Prediction
# =============================

@app.post("/sentiment")
def sentiment(request: ReviewRequest):

    result = predict_sentiment(
        request.review
    )

    return {
        "review": request.review,
        "sentiment": result
    }

# to test the review

@app.get("/sentiment-test")
def sentiment_test():

    review = "This product is excellent and works perfectly"

    result = predict_sentiment(
        review
    )

    return {
        "review": review,
        "sentiment": result
    }


@app.get("/sentiment-test")
def sentiment_test():

    review = "This product is excellent and works perfectly"

    result = predict_sentiment(
        review
    )

    return {
        "review": review,
        "sentiment": result
    }

@app.get("/sentiment-test")
def sentiment_test():

    review = "This product is excellent and works perfectly"

    result = predict_sentiment(
        review
    )

    return {
        "review": review,
        "sentiment": result
    }


@app.get("/sentiment-test")
def sentiment(request: ReviewRequest):

    review = "This product is excellent and works perfectly"

    result = predict_sentiment(
        review
    )

    return {
        "review": review,
        "sentiment": result
    }



# =============================
# AI Business Insights
# =============================

@app.get("/insights")
def insights():

    # =================================
    # 1. Load data
    # =================================

    data = prepare_data()

    # =================================
    # 2. Load sentiment model ONCE
    # =================================

    sentiment_model = load_model()

    # =================================
    # 3. Predict all reviews at once
    # =================================

    reviews = (
        data["review_text"]
        .fillna("")
        .astype(str)
    )

    data["sentiment"] = (
        sentiment_model.predict(
            reviews
        )
    )

    # =================================
    # 4. Count sentiment
    # =================================

    sentiment_counts = (
        data["sentiment"]
        .value_counts()
        .to_dict()
    )

    positive = sentiment_counts.get(
        "positive",
        0
    )

    neutral = sentiment_counts.get(
        "neutral",
        0
    )

    negative = sentiment_counts.get(
        "negative",
        0
    )

    # =================================
    # 5. Business Metrics
    # =================================

    total_orders = data[
        "order_id"
    ].nunique()

    total_revenue = (
        pd.to_numeric(
            data["revenue"],
            errors="coerce"
        )
        .fillna(0)
        .sum()
    )

    total_reviews = len(data)

    average_rating = (
        pd.to_numeric(
            data["rating"],
            errors="coerce"
        )
        .mean()
    )

    total_returns = (
        data["returned"]
        .astype(str)
        .str.lower()
        .isin([
            "yes",
            "true",
            "1"
        ])
        .sum()
    )

    # =================================
    # 6. Customer Feedback
    # =================================

    feedback_columns = [
        "product_review",
        "review_text",
        "rating",
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
        .head(30)
        .to_string(index=False)
    )

    # =================================
    # 7. Create Gemini Summary
    # =================================

    summary = f"""
Amazon Business Intelligence Summary

Business Metrics:

Total Orders:
{total_orders}

Total Revenue:
{total_revenue:.2f}

Total Reviews:
{total_reviews}

Average Rating:
{average_rating:.2f}

Total Returns:
{total_returns}

Customer Sentiment:

Positive:
{positive}

Neutral:
{neutral}

Negative:
{negative}

Customer Feedback:

{feedback}
"""

    # =================================
    # 8. Send to Gemini
    # =================================

    result = generate_insights(
        summary
    )

    # =================================
    # 9. Return response
    # =================================

    return {
        "summary": {
            "total_orders": total_orders,
            "total_revenue": round(
                float(total_revenue),
                2
            ),
            "total_reviews": total_reviews,
            "average_rating": round(
                float(average_rating),
                2
            ),
            "total_returns": int(
                total_returns
            ),
            "sentiment": {
                "positive": int(
                    positive
                ),
                "neutral": int(
                    neutral
                ),
                "negative": int(
                    negative
                )
            }
        },

        "insights": result
    }
