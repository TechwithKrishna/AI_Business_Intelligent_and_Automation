# LLM_Recommendation_and_Insights/ai.py

import os

from dotenv import load_dotenv
from google import genai


# ---------------------------------
# Load environment variables
# ---------------------------------

load_dotenv()


# ---------------------------------
# Gemini API Key
# ---------------------------------

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not set in .env"
    )


# ---------------------------------
# Gemini Client
# ---------------------------------

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ---------------------------------
# Gemini Model
# ---------------------------------

MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)


# ---------------------------------
# Generate Business Insights
# ---------------------------------

def generate_insights(data_summary):

    prompt = f"""
You are an expert business intelligence analyst.

Analyze the following customer and business data:

{data_summary}

Provide:

1. Main customer problems
2. Recurring issues
3. Product improvement suggestions
4. Marketing suggestions
5. Overall business insight

Rules:

- Use only the data provided.
- Do not invent statistics.
- Clearly separate observations from recommendations.
- Keep the response concise.
- Make recommendations actionable.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


# ---------------------------------
# Product Recommendation
# ---------------------------------

def generate_product_recommendation(
    product_name,
    reviews,
    sentiment
):

    prompt = f"""
You are an expert product and marketing analyst.

Analyze this product using customer feedback.

Product:
{product_name}

Customer Reviews:
{reviews}

Sentiment:
{sentiment}

Provide:

1. Main customer problem
2. Recurring issue
3. Possible reason
4. Product improvement
5. Marketing recommendation

Rules:

- Use only the information provided.
- Do not invent statistics.
- Keep the answer concise.
- Make recommendations actionable.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


# ---------------------------------
# Test
# ---------------------------------

if __name__ == "__main__":

    data = """
Product: Wireless Headphones

Total Reviews: 150

Positive: 80
Neutral: 25
Negative: 45

Common complaints:
- Battery drains quickly
- Bluetooth connection problems
- Poor build quality
"""

    result = generate_insights(data)

    print(
        "\n===== AI BUSINESS INSIGHTS =====\n"
    )

    print(result)
