import os
import pandas as pd


# ==============================
# File paths
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ORDERS_FILE = os.path.join(BASE_DIR, "orders.csv")
REVIEWS_FILE = os.path.join(BASE_DIR, "reviews.csv")


# ==============================
# Load Orders
# ==============================

def load_orders():

    orders = pd.read_csv(ORDERS_FILE)

    # Convert date
    orders["date"] = pd.to_datetime(
        orders["date"],
        errors="coerce"
    )

    # Convert quantity and price to numbers
    orders["quantity"] = pd.to_numeric(
        orders["quantity"],
        errors="coerce"
    ).fillna(0)

    orders["price"] = pd.to_numeric(
        orders["price"],
        errors="coerce"
    ).fillna(0)

    # Calculate revenue
    orders["revenue"] = (
        orders["quantity"] * orders["price"]
    )

    return orders


# ==============================
# Load Reviews
# ==============================

def load_reviews():

    reviews = pd.read_csv(REVIEWS_FILE)

    # Convert date
    reviews["date"] = pd.to_datetime(
        reviews["date"],
        errors="coerce"
    )

    # Convert rating
    reviews["rating"] = pd.to_numeric(
        reviews["rating"],
        errors="coerce"
    )

    # Clean review text
    reviews["review_text"] = (
        reviews["review_text"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    return reviews


# ==============================
# Sentiment
# ==============================

def create_sentiment(rating):

    if pd.isna(rating):
        return "neutral"

    if rating >= 4:
        return "positive"

    if rating == 3:
        return "neutral"

    return "negative"


# ==============================
# Prepare Data
# ==============================

def prepare_data():

    orders = load_orders()
    reviews = load_reviews()

    # Create sentiment
    reviews["sentiment"] = reviews["rating"].apply(
        create_sentiment
    )

    # Merge orders and reviews
    data = reviews.merge(
        orders,
        on="order_id",
        how="left",
        suffixes=("_review", "_order")
    )

    return data


# ==============================
# Statistics
# ==============================

def get_statistics(data):

    statistics = {

        "total_orders":
            data["order_id"].nunique(),

        "total_revenue":
            data["revenue"].sum(),

        "total_quantity":
            data["quantity"].sum(),

        "total_reviews":
            len(data),

        "average_rating":
            data["rating"].mean(),

        "positive_reviews":
            (data["sentiment"] == "positive").sum(),

        "neutral_reviews":
            (data["sentiment"] == "neutral").sum(),

        "negative_reviews":
            (data["sentiment"] == "negative").sum(),

        "total_returns":
            (
                data["returned"]
                .astype(str)
                .str.lower()
                .isin(["yes", "true", "1"])
                .sum()
            )
    }

    return statistics


# ==============================
# Test
# ==============================

if __name__ == "__main__":

    data = prepare_data()

    print("\n==============================")
    print("DATA LOADED SUCCESSFULLY")
    print("==============================")

    print("\nRows:", len(data))

    print("\nColumns:")
    print(data.columns.tolist())

    print("\nSample Data:")

    print(
        data[
            [
                "order_id",
                "product_review",
                "rating",
                "review_text",
                "sentiment",
                "quantity",
                "price",
                "revenue"
            ]
        ].head()
    )

    print("\n==============================")
    print("STATISTICS")
    print("==============================")

    statistics = get_statistics(data)

    for key, value in statistics.items():

        if isinstance(value, float):
            print(f"{key}: {value:.2f}")

        else:
            print(f"{key}: {value}")
