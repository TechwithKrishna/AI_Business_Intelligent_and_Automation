## AI Business Intelligent and Automation

An AI-powered business intelligence and automation system that analyzes customer reviews and order data to identify recurring issues, measure customer sentiment, generate business recommendations, and automate dashboard insights.

The project combines Python, NLP, PostgreSQL, Flask API, Streamlit, and Google Gemini LLM to transform raw business data into actionable insights.

## 🚀 Project Overview

The system is designed around two major business use cases:

1. Customer Feedback Intelligence

The Customer Feedback Intelligence module analyzes customer reviews along with order information to understand customer experiences and identify recurring issues.

It can:

Analyze customer reviews using NLP.
Perform sentiment analysis.
Identify positive and negative customer feedback.
Detect recurring complaints and product issues.
Connect reviews with order and product information.
Identify trends in customer satisfaction.
Generate AI-powered recommendations.
Provide product and marketing improvement suggestions.
2. Dashboard Automation Agent

The Dashboard Automation Agent automates business reporting and helps consolidate information from multiple data sources.

It can:

Process order and review data.
Calculate important business metrics.
Generate business summaries.
Identify significant trends.
Detect potential business issues.
Generate AI-based insights.
Provide information for business dashboards.
Reduce manual reporting and analysis.
🛠️ Tech Stack
Python — Core programming language.
NLP — Natural Language Processing for customer review analysis.
Google Gemini — LLM for recommendations, summaries, and business insights.
PostgreSQL — Database for storing and querying business data.
Flask — Backend API for serving application functionality.
Streamlit — Interactive business intelligence dashboard.
Pandas — Data processing and analysis.
dotenv — Environment variable and API-key management.
## 📊 Dataset

The project primarily works with two types of datasets.

Orders Dataset

The orders dataset contains information about customer purchases.

Typical fields may include:

Order ID
Customer ID
Product ID
Product Name
Order Date
Quantity
Price
Total Amount
Order Status
Customer Reviews Dataset

The reviews dataset contains customer feedback about products or orders.

Typical fields may include:

Review ID
Customer ID
Product ID
Rating
Review Text
Review Date

By combining order information with customer reviews, the system can understand not only what customers are saying, but also which products, orders, or business segments are associated with that feedback.

## 🧠 AI and NLP Workflow
                 ┌─────────────────────┐
                 │    Orders Dataset   │
                 └──────────┬──────────┘
                            │
                 ┌──────────▼──────────┐
                 │   Reviews Dataset   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Preprocessing    │
                 │ Cleaning & Transform│
                 └──────────┬──────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
   ┌────────────────────┐       ┌─────────────────────┐
   │ NLP Sentiment      │       │     PostgreSQL      │
   │      Model         │       │      Database       │
   └─────────┬──────────┘       └──────────┬──────────┘
             │                             │
             └─────────────┬───────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ LLM Recommendation &     │
              │       Insights           │
              │      Google Gemini       │
              └─────────────┬────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      AI Agent       │
                 │ Business Automation │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Flask API         │
                 │ Backend Services    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     Streamlit       │
                 │     Dashboard       │
                 └─────────────────────┘

## 📁 Project Structure
AI-Business-Intelligent-and-Automation/
│
├── .venv/
│   └── Python virtual environment
│
├── AI Agent/
│   └── AI agent components for business automation
│
├── Dashboard/
│   └── Streamlit dashboard and visualization
│
├── data/
│   └── Orders and customer review datasets
│
├── LLM_Recommendation_and_Insights/
│   └── Gemini LLM-based recommendations and business insights
│
├── NLP_Sentiment_Model/
│   └── NLP models and sentiment analysis for customer reviews
│
├── PostgreSQL/
│   └── PostgreSQL database integration and operations
│
├── Preprocessing/
│   └── Data cleaning, transformation, and preprocessing
│
├── utils/
│   └── Common utility functions used across the project
│
├── .env
│   └── Environment variables and API configuration
│
├── README.md
│   └── Project documentation
│
└── requirements.txt
    └── Python dependencies

## 🧩 Project Components
Preprocessing

The Preprocessing module prepares raw datasets for further analysis.

Responsibilities include:

Data cleaning.
Handling missing values.
Data transformation.
Removing duplicate records.
Preparing review text for NLP.
Preparing order data for analysis.
Combining relevant datasets.
NLP Sentiment Model

The NLP_Sentiment_Model module analyzes customer reviews.

It is responsible for:

Text preprocessing.
Sentiment classification.
Identifying positive reviews.
Identifying negative reviews.
Measuring customer sentiment.
Supporting review trend analysis.
PostgreSQL

The PostgreSQL module provides database functionality for storing and managing business data.

It can store:

Customer information.
Orders.
Products.
Reviews.
Sentiment results.
Business metrics.
AI-generated insights.
LLM Recommendation and Insights

The LLM_Recommendation_and_Insights module uses Google Gemini to convert analyzed data into understandable business recommendations.

The LLM can:

Summarize customer feedback.
Explain important trends.
Identify recurring issues.
Generate business recommendations.
Suggest product improvements.
Suggest marketing improvements.
Generate management-level summaries.
AI Agent

The AI Agent module provides automation capabilities.

The agent can coordinate different parts of the system to:

Collect data.
Process information.
Analyze customer feedback.
Generate insights.
Produce business summaries.
Support automated reporting.
Flask API

The Flask API acts as the backend service layer of the application.

It is responsible for:

Receiving requests from the dashboard.
Running backend analysis.
Connecting application components.
Providing data and insights to the frontend.
Exposing API endpoints for the Streamlit application.
Streamlit Dashboard

The Streamlit application provides the interactive user interface.

The dashboard can display:

Total Orders.
Total Revenue.
Average Order Value.
Customer Ratings.
Positive Sentiment %.
Negative Sentiment %.
Most Complained Products.
Most Loved Products.
Review Trends.
Order Trends.
Product Performance.
AI Recommendations.
## ⚙️ Installation
1. Clone the Repository
git clone <repository-url>
cd AI-Business-Intelligent-and-Automation

2. Create Virtual Environment
python -m venv .venv

Windows
.venv\Scripts\activate

Linux/macOS
source .venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

## 🔐 Environment Variables

Create a .env file in the project root.

Example:

GEMINI_API_KEY=your_gemini_api_key


If PostgreSQL is being used, configure the database as well:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password


Do not commit your .env file or API keys to GitHub.

## ▶️ Running the Project

After installing all dependencies and configuring the .env file, the project requires two terminals to run the backend API and Streamlit dashboard.

Terminal 1 — Start Flask API

Open the first terminal and activate the virtual environment:

.venv\Scripts\activate


Then start the Flask API:

flask run


The Flask backend will start and provide the API services required by the dashboard.

Keep this terminal running.

Terminal 2 — Start Streamlit Dashboard

Open a second terminal in the project directory.

Activate the virtual environment:

.venv\Scripts\activate


Then start the Streamlit dashboard:

streamlit run Dashboard/app.py


If your Streamlit entry-point file has a different name or location, replace Dashboard/app.py with the correct file path.

Keep this terminal running as well.

## 🖥️ Application Architecture

Once both services are running:

┌──────────────────────┐
│     Streamlit        │
│      Dashboard       │
└──────────┬───────────┘
           │
           │ HTTP Requests
           ▼
┌──────────────────────┐
│      Flask API       │
│   Backend Services   │
└──────────┬───────────┘
           │
     ┌─────┴─────┐
     │           │
     ▼           ▼
┌─────────┐  ┌──────────────┐
│PostgreSQL│  │ AI / NLP /   │
│ Database │  │ Gemini LLM   │
└─────────┘  └──────────────┘


The Streamlit dashboard communicates with the Flask API, while the backend interacts with the database, NLP models, AI agent, and Gemini LLM.

## 📈 Example Business Insights

The system can generate insights such as:

Negative reviews for Product A have increased this month, with most complaints related to packaging damage.

Product B has strong positive sentiment, with customers frequently mentioning product quality and value.

Repeat customers are generating a higher average order value compared with first-time customers.

Products with high ratings and positive customer sentiment can be prioritized in marketing campaigns.

## 💡 Business Recommendations

Based on the combined analysis of orders and reviews, the system can recommend:

Improve product quality.
Improve packaging.
Optimize shipping processes.
Update product descriptions.
Improve customer support.
Promote highly rated products.
Investigate products with increasing negative sentiment.
Optimize marketing campaigns.
Identify products with strong repeat-purchase behavior.
## 🎯 Project Goals

The primary goals of AI Business Intelligent and Automation are:

Automate customer feedback analysis.
Understand customer sentiment.
Identify recurring product and service issues.
Combine customer reviews with order information.
Generate actionable business recommendations.
Automate business reporting.
Reduce manual data analysis.
Provide useful insights through dashboards.
Help businesses make data-driven decisions.
## 🔮 Future Enhancements

Possible future improvements include:

Real-time data processing.
Automated dashboard refresh.
Email and Slack notifications.
Conversational AI business assistant.
Predictive sales analysis.
Customer churn prediction.
Advanced customer segmentation.
Review trend forecasting.
Multi-language sentiment analysis.
Automated weekly and monthly business reports.
Integration with CRM and e-commerce platforms.
Real-time anomaly detection.
## 🔒 Security

Sensitive information such as API keys, database passwords, and credentials should be stored in environment variables.

Recommended .gitignore entries:

.env
.venv/
__pycache__/
*.pyc

## 📌 Summary

AI Business Intelligent and Automation is an end-to-end AI-powered business analytics system that combines:

Orders
   +
Customer Reviews
   +
Python
   +
NLP
   +
PostgreSQL
   +
Google Gemini LLM
   +
Flask API
   +
Streamlit
   =
AI-Powered Business Intelligence & Automation


The system transforms raw order and customer review data into sentiment analysis, recurring issue detection, business insights, recommendations, and automated dashboard information.

The overall workflow is:

Data → Preprocessing → NLP → PostgreSQL → Gemini → AI Agent → Flask API → Streamlit Dashboard

The project helps businesses move from:

Raw Data → Meaningful Insights → Actionable Decisions
