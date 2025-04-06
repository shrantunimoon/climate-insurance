# climate-insurance

summarized insights on climate risk and insurance policies from trusted news sources. This interactive Streamlit dashboard fetches articles from multiple APIs, summarizes them using NLP, and presents them in a user-friendly format.

🚀 Features
🔍 Search News: Enter a custom search query (default is "climate risk insurance").

🌐 Multiple Sources:

Tavily API for enriched, AI-powered search results.

Google News API for global news coverage.

🧠 Summarization: Uses facebook/bart-large-cnn model from Hugging Face to auto-summarize articles.

💾 Caching: Efficient data fetching using @st.cache_data.

📋 Clean Layout: Read summaries, sources, and publish dates in a structured and scrollable format.

📦 Technologies Used
Streamlit

Hugging Face Transformers

LangChain Tavily Tool

Tavily API

Google News API

Python 3.9+

🛠️ Setup Instructions
Clone the repository
git clone https://github.com/yourusername/climate-risk-dashboard.git
cd climate-risk-dashboard

Install dependencies
pip install -r requirements.txt

Set your API keys
Replace the placeholder keys in the Python file:
TAVILY_API_KEY = "your_tavily_api_key"
GOOGLE_NEWS_API_KEY = "your_google_news_api_key"

Run the app
streamlit run app.py

🔑 API Keys Required
Tavily API Key: Get it from Tavily

Google News API Key: Get it from NewsAPI.org

📸 Preview

A sleek dashboard for staying updated on climate risk news.

🙌 Credits
Summarization powered by Facebook's BART model

Real-time news via Tavily and Google News

Built with ❤️ using Streamlit

📃 License
MIT License. Feel free to fork and adapt for your own use.









