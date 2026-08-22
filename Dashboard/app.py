import streamlit as st
import requests
import pandas as pd


# ==========================================
# Configuration
# ==========================================

API_URL = "http://127.0.0.1:8000"


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI Business Intelligence",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# Custom CSS
# ==========================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #1f2937;
    }

    .subtitle {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# Header
# ==========================================

st.markdown(
    '<div class="main-title">📊 AI Business Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Customer Feedback Intelligence & Business Analytics'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# Check API
# ==========================================

try:

    health_response = requests.get(
        f"{API_URL}/health",
        timeout=5
    )

    api_running = (
        health_response.status_code == 200
    )

except requests.exceptions.RequestException:

    api_running = False


if not api_running:

    st.error(
        "FastAPI backend is not running."
    )

    st.code(
        "uv run uvicorn api:app --reload"
    )

    st.stop()


# ==========================================
# Sidebar
# ==========================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard",
        "Customer Data",
        "AI Insights",
        "Sentiment Analysis"
    ]
)


# ==========================================
# Dashboard
# ==========================================

if page == "Dashboard":

    st.header("📈 Business Dashboard")

    try:

        response = requests.get(
            f"{API_URL}/insights",
            timeout=120
        )

        if response.status_code != 200:

            st.error(
                f"API Error: {response.status_code}"
            )

            st.code(
                response.text
            )

            st.stop()

        result = response.json()

        summary = result["summary"]

        sentiment = summary["sentiment"]

        # ----------------------------------
        # Metrics
        # ----------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Total Orders",
                f"{summary['total_orders']:,}"
            )

        with col2:

            st.metric(
                "Total Revenue",
                f"${summary['total_revenue']:,.2f}"
            )

        with col3:

            st.metric(
                "Total Reviews",
                f"{summary['total_reviews']:,}"
            )

        with col4:

            st.metric(
                "Average Rating",
                f"{summary['average_rating']:.2f} ⭐"
            )

        st.divider()

        # ----------------------------------
        # Returns
        # ----------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("🔄 Returns")

            st.metric(
                "Total Returns",
                f"{summary['total_returns']:,}"
            )

        with col2:

            st.subheader("😊 Customer Sentiment")

            sentiment_df = pd.DataFrame(
                {
                    "Sentiment": [
                        "Positive",
                        "Neutral",
                        "Negative"
                    ],
                    "Count": [
                        sentiment["positive"],
                        sentiment["neutral"],
                        sentiment["negative"]
                    ]
                }
            )

            st.bar_chart(
                sentiment_df.set_index(
                    "Sentiment"
                )
            )

        st.divider()

        # ----------------------------------
        # Quick AI Insight
        # ----------------------------------

        st.subheader(
            "🤖 AI Business Insights"
        )

        st.write(
            result["insights"]
        )

    except requests.exceptions.Timeout:

        st.error(
            "The AI analysis took too long. "
            "Please try again."
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )


# ==========================================
# Customer Data
# ==========================================

elif page == "Customer Data":

    st.header("🛒 Customer & Order Data")

    try:

        response = requests.get(
            f"{API_URL}/data",
            timeout=30
        )

        if response.status_code != 200:

            st.error(
                "Unable to load data."
            )

            st.stop()

        result = response.json()

        data = pd.DataFrame(
            result["data"]
        )

        st.write(
            f"Total rows: {result['total_rows']:,}"
        )

        st.dataframe(
            data,
            use_container_width=True,
            height=500
        )

    except Exception as e:

        st.error(
            f"Error loading data: {e}"
        )


# ==========================================
# AI Insights
# ==========================================

elif page == "AI Insights":

    st.header("🤖 AI Business Insights")

    st.write(
        "Gemini analyzes customer feedback, "
        "sentiment, revenue, orders and returns."
    )

    if st.button(
        "Generate AI Insights",
        type="primary"
    ):

        with st.spinner(
            "Analyzing business data with Gemini..."
        ):

            try:

                response = requests.get(
                    f"{API_URL}/insights",
                    timeout=120
                )

                if response.status_code != 200:

                    st.error(
                        f"API Error: {response.status_code}"
                    )

                    st.code(
                        response.text
                    )

                else:

                    result = response.json()

                    st.success(
                        "Insights generated successfully!"
                    )

                    st.markdown(
                        result["insights"]
                    )

            except requests.exceptions.Timeout:

                st.error(
                    "Gemini took too long to respond. "
                    "Please try again."
                )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )


# ==========================================
# Sentiment Analysis
# ==========================================

elif page == "Sentiment Analysis":

    st.header("💬 Customer Sentiment Analysis")

    review = st.text_area(
        "Enter a customer review:",
        placeholder=(
            "Example: The product quality is excellent "
            "and delivery was very fast."
        ),
        height=150
    )

    if st.button(
        "Analyze Sentiment",
        type="primary"
    ):

        if not review.strip():

            st.warning(
                "Please enter a review."
            )

        else:

            try:

                response = requests.post(
                    f"{API_URL}/sentiment",
                    json={
                        "review": review
                    },
                    timeout=30
                )

                if response.status_code != 200:

                    st.error(
                        f"API Error: {response.status_code}"
                    )

                    st.code(
                        response.text
                    )

                else:

                    result = response.json()

                    sentiment = result[
                        "sentiment"
                    ]

                    # --------------------------
                    # Display result
                    # --------------------------

                    if sentiment == "positive":

                        st.success(
                            "😊 Positive"
                        )

                    elif sentiment == "negative":

                        st.error(
                            "😞 Negative"
                        )

                    else:

                        st.info(
                            "😐 Neutral"
                        )

                    st.write(
                        f"**Sentiment:** {sentiment}"
                    )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )
