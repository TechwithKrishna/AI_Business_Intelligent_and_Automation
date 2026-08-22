import os
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# ==================================================
# PATHS
# ==================================================

CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

PROJECT_DIR = os.path.dirname(
    CURRENT_DIR
)

# Reviews CSV
REVIEWS_PATH = os.path.join(
    PROJECT_DIR,
    "utils",
    "reviews.csv"
)

# Model folder
MODEL_DIR = os.path.join(
    CURRENT_DIR,
    "models"
)

# Model file
MODEL_PATH = os.path.join(
    MODEL_DIR,
    "sentiment_model.pkl"
)


# ==================================================
# CREATE SENTIMENT FROM RATING
# ==================================================

def rating_to_sentiment(rating):

    if pd.isna(rating):
        return "neutral"

    rating = float(rating)

    if rating >= 4:
        return "positive"

    elif rating == 3:
        return "neutral"

    else:
        return "negative"


# ==================================================
# LOAD REVIEWS
# ==================================================

def load_data():

    if not os.path.exists(REVIEWS_PATH):

        raise FileNotFoundError(
            f"reviews.csv not found at:\n{REVIEWS_PATH}"
        )

    df = pd.read_csv(
        REVIEWS_PATH
    )

    # Check columns

    required_columns = [
        "rating",
        "review_text"
    ]

    for column in required_columns:

        if column not in df.columns:

            raise ValueError(
                f"Missing column '{column}' "
                f"in reviews.csv"
            )

    # Remove missing values

    df = df.dropna(
        subset=[
            "rating",
            "review_text"
        ]
    )

    # Convert review text to string

    df["review_text"] = (
        df["review_text"]
        .astype(str)
        .str.strip()
    )

    # Remove empty reviews

    df = df[
        df["review_text"] != ""
    ]

    # Create sentiment label

    df["sentiment"] = (
        df["rating"]
        .apply(rating_to_sentiment)
    )

    return df


# ==================================================
# TRAIN MODEL
# ==================================================

def train_model():

    print("=" * 50)
    print("TRAINING SENTIMENT MODEL")
    print("=" * 50)

    # Load data

    df = load_data()

    print(
        f"\nTotal reviews: {len(df)}"
    )

    # Show sentiment distribution

    print(
        "\nSentiment distribution:"
    )

    print(
        df["sentiment"].value_counts()
    )

    # Input

    X = df[
        "review_text"
    ]

    # Output

    y = df[
        "sentiment"
    ]

    # ----------------------------------------------
    # Train/Test Split
    # ----------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=0.2,

        random_state=42,

        stratify=y
    )

    # ----------------------------------------------
    # NLP Model
    # ----------------------------------------------

    model = Pipeline([

        (
            "tfidf",

            TfidfVectorizer(

                lowercase=True,

                stop_words="english",

                max_features=10000,

                ngram_range=(1, 2)
            )
        ),

        (
            "classifier",

            LogisticRegression(

                max_iter=1000
            )
        )
    ])

    # ----------------------------------------------
    # Train
    # ----------------------------------------------

    print(
        "\nTraining model..."
    )

    model.fit(
        X_train,
        y_train
    )

    # ----------------------------------------------
    # Evaluate
    # ----------------------------------------------

    predictions = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(
        f"\nAccuracy: {accuracy:.2f}"
    )

    print(
        "\nClassification Report:"
    )

    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )

    # ----------------------------------------------
    # Save model
    # ----------------------------------------------

    os.makedirs(
        MODEL_DIR,
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    print(
        "\nModel saved successfully:"
    )

    print(
        MODEL_PATH
    )

    return model


# ==================================================
# LOAD TRAINED MODEL
# ==================================================

def load_model():

    # If model doesn't exist,
    # train it automatically.

    if not os.path.exists(
        MODEL_PATH
    ):

        print(
            "Sentiment model not found."
        )

        print(
            "Training new model..."
        )

        return train_model()

    print(
        "Loading trained sentiment model..."
    )

    return joblib.load(
        MODEL_PATH
    )


# ==================================================
# PREDICT ONE REVIEW
# ==================================================

def predict_sentiment(text):

    if text is None:

        return "neutral"

    text = str(text).strip()

    if not text:

        return "neutral"

    model = load_model()

    prediction = model.predict(
        [text]
    )

    return prediction[0]


# ==================================================
# PREDICT MULTIPLE REVIEWS
# ==================================================

def predict_reviews(reviews):

    model = load_model()

    reviews = (
        pd.Series(reviews)
        .fillna("")
        .astype(str)
    )

    return model.predict(
        reviews
    )


# ==================================================
# TEST MODEL
# ==================================================

if __name__ == "__main__":

    # Train model

    model = train_model()

    # Test reviews

    test_reviews = [

        "I absolutely love this product!",

        "The product is okay.",

        "Very poor quality and stopped working.",

        "Excellent product and fast delivery!",

        "I am disappointed with this purchase."

    ]

    predictions = model.predict(
        test_reviews
    )

    print(
        "\nTest Predictions:"
    )

    print(
        "-" * 50
    )

    for review, sentiment in zip(
        test_reviews,
        predictions
    ):

        print(
            f"{sentiment.upper():8} -> {review}"
        )
