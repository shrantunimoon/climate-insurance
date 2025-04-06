import streamlit as st
import requests
from transformers import pipeline
from langchain_community.tools.tavily_search import TavilySearchResults

TAVILY_API_KEY = "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"
GOOGLE_NEWS_API_KEY = "06d8341797d3411b9f4375166d48a4b8"

tavily_tool = TavilySearchResults(tavily_api_key=TAVILY_API_KEY, max_results=5)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@st.cache_data
def fetch_tavily_news(query):
    try:
        response = tavily_tool.invoke({"query": query})
        print("Tavily response:", response)

        if isinstance(response, list):
            articles = response
        else:
            articles = response.get("results", [])

        return [
            {
                "title": article.get("title", "No title"),
                "source": article.get("source", "Unknown source"),
                "date": article.get("date", "No date"),
                "summary": article.get("snippet", "No summary"),
            }
            for article in articles
        ]
    except Exception as e:
        st.error(f"Error fetching Tavily news: {e}")
        return []

@st.cache_data
def fetch_google_news(query):
    try:
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={GOOGLE_NEWS_API_KEY}"
        response = requests.get(url).json()
        return [
            {
                "title": article["title"],
                "source": article["source"]["name"],
                "date": article["publishedAt"],
                "summary": article["description"],
            }
            for article in response.get("articles", [])
        ]
    except Exception as e:
        st.error(f"Error fetching Google news: {e}")
        return []

@st.cache_data
def summarize_news(articles):
    summarized_articles = []
    for article in articles:
        text = article["summary"]
        if text:
            try:
                summary = summarizer(text, max_length=50, min_length=30, do_sample=False)[0]["summary_text"]
            except Exception as e:
                st.error(f"Error summarizing: {e}")
                summary = "Summary failed."
        else:
            summary = "No summary available."

        summarized_articles.append({
            "title": article["title"],
            "source": article["source"],
            "date": article["date"],
            "summary": summary,
        })

    return summarized_articles

st.title("🌍 Climate Risk Insurance Dashboard")
st.write("Get the latest news and insights on climate risk and insurance policies.")

query = st.text_input("Enter a search query:", "climate risk insurance")

if "summarized_news" not in st.session_state:
    st.session_state.summarized_news = []

if st.button("Fetch News"):
    with st.spinner("Fetching and summarizing latest news..."):
        tavily_news = fetch_tavily_news(query)
        google_news = fetch_google_news(query)
        all_news = tavily_news + google_news
        st.session_state.summarized_news = all_news  


for article in st.session_state.summarized_news:
    st.write(f"**{article['title']}**")
    st.caption(f"{article['source']} | {article['date']}")
    st.write(article["summary"])
    st.markdown("---")
    

st.sidebar.header("About")
st.sidebar.info(
    "This dashboard fetches real-time news on climate risk and insurance, summarizes key insights, and presents structured reports."
)