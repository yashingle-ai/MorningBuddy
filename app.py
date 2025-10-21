import streamlit as st
import random
from applications import temperature_of_city, get_news, news_summarizer, smart_plan


# Page Config

st.set_page_config(
    page_title="🌤️ Morning Buddy",
    page_icon="☀️",
    layout="wide"
)


# Custom CSS for better visibility & HCI

st.markdown("""
    <style>
        /* App background */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(to right, #f0f4f8, #ffffff);
            color: #111111;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Sidebar style */
        [data-testid="stSidebar"] {
            background-color: #0078D7;
            color: white;
            padding: 20px;
        }
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label {
            color: white !important;
        }
        [data-testid="stSidebar"] .stRadio > label {
            color: white;
        }

        /* Buttons */
        .stButton>button {
            background-color: #0078D7;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 18px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #005a9e;
            color: white;
            transform: scale(1.02);
        }

        /* Headings */
        h1 {
            color: #003366;
            font-size: 36px;
        }
        h2 {
            color: #004080;
            font-size: 28px;
        }

        /* Quote box */
        .quote-box {
            background-color: #e8f0fe;
            border-left: 6px solid #0078D7;
            padding: 20px;
            border-radius: 8px;
            font-style: italic;
            font-size: 18px;
        }

        /* News article card */
        .news-card {
            background-color: #f7f9fc;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }

        /* Input box */
        .stTextInput>div>input {
            background-color: #f0f4f8;
            color: #111111;
            border-radius: 6px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)


# Helper Functions

def get_random_quote():
    quotes = [
        "The sun is a daily reminder that we too can rise again and shine our own light.",
        "An early-morning walk is a blessing for the whole day.",
        "Rise up, start fresh, see the bright opportunity in each new day.",
        "Write it on your heart that every day is the best day in the year.",
        "Lose an hour in the morning, and you will spend all day looking for it.",
        "Today’s goals: Coffee and kindness."
    ]
    return random.choice(quotes)


# Pages

def home_page():
    st.title("🌤️ Your Morning Buddy")
    st.markdown("---")
    st.markdown(f"<div class='quote-box'>“{get_random_quote()}”</div>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1500382017468-9049fed747ef", caption="A beautiful start to your day ☀️", use_container_width=True)
    st.markdown("---")
    st.info("✨ Use the sidebar to explore Weather, News, and Smart Planner!")

def weather_page():
    st.header("🌦️ Check Today's Weather")
    city = st.text_input("Enter your city name:")
    if st.button("Get Weather"):
        if city.strip():
            with st.spinner("Fetching weather data..."):
                try:
                    weather = temperature_of_city(city)
                    st.success("Weather fetched successfully!")
                    st.subheader(f"🌇 Weather in {city.capitalize()}")
                    st.write(weather)
                except Exception as e:
                    st.error(f"Error fetching weather: {e}")
        else:
            st.warning("Please enter a city name!")

def news_page():
    st.header("📰 Latest News by Interest")
    topic = st.text_input("Enter topic (e.g., Technology, Sports, Health):", "Technology")
    if st.button("Fetch News"):
        if topic.strip():
            with st.spinner("Fetching news..."):
                try:
                    articles = get_news(topic)
                    if not articles:
                        st.error("No articles found.")
                        return
                    st.success("Top 5 latest articles:")
                    for i, a in enumerate(articles[:5]):
                        st.markdown(f"<div class='news-card'><h4>{i+1}. {a['title']}</h4>", unsafe_allow_html=True)
                        if a.get("urlToImage"):
                            st.image(a["urlToImage"], use_column_width=True)
                        st.markdown(f"[Read Full Article]({a['url']})")
                        with st.expander("📝 Summary"):
                            try:
                                summary = news_summarizer(a["url"])
                                st.write(summary)
                            except:
                                st.write("Unable to summarize this article.")
                        st.markdown("</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error fetching news: {e}")
        else:
            st.warning("Please enter a topic!")

def planner_page():
    st.header("🗓️ Smart Day Planner")
    city = st.text_input("Enter your city name:")
    if st.button("Generate Plan"):
        if city.strip():
            with st.spinner("Generating your day's plan..."):
                try:
                    plan = smart_plan(city)
                    st.success("Your personalized itinerary is ready!")
                    st.write(plan)
                except Exception as e:
                    st.error(f"Error generating plan: {e}")
        else:
            st.warning("Please enter a city name!")


# Sidebar Navigation

st.sidebar.title("🔍 Navigation")
option = st.sidebar.radio("Choose a page:", ["🏠 Home", "🌦️ Weather", "📰 News", "🗓️ Planner"])
st.sidebar.markdown("---")
st.sidebar.caption("Created with ❤️ using Streamlit & Gemini AI")


# Page Routing

if option == "🏠 Home":
    home_page()
elif option == "🌦️ Weather":
    weather_page()
elif option == "📰 News":
    news_page()
elif option == "🗓️ Planner":
    planner_page()
