````markdown
# 🌤️ Morning Buddy: Your Personal AI Dashboard

Morning Buddy is a smart, multi-page Streamlit dashboard designed to kickstart your day. It acts as a personal assistant, providing you with the latest weather, top news headlines, and a personalized daily plan, all powered by the Google Gemini AI model and its powerful function-calling and grounding capabilities.

## ✨ Features

* **🌦️ Smart Weather Reports:** Get a human-readable weather report for any city, not just raw JSON data. (Powered by Gemini function calling with the OpenWeather API).
* **📰 AI-Summarized News:** Fetch the top 5 news articles on any topic (e.g., "Technology," "Health") and get an instant AI-powered summary for each article. (Powered by NewsAPI and Gemini).
* **🗓️ Personalized Day Planner:** Generate a complete day's itinerary for any city. This plan intelligently combines the forecasted weather, top places to visit, and local events. (Powered by Gemini function calling with Google Search and SerpApi).
* **🎨 Custom Interface:** A clean, multi-page Streamlit app with custom CSS for a friendly and modern user experience.

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Backend:** [Python](https://www.python.org/)
* **AI Model:** Google Gemini (`gemini-2.5-flash` & `gemini-2.5-flash-lite`)
* **Core Libraries:**
    * `google-generativeai` (for Gemini API)
    * `requests` (for HTTP requests)
    * `python-dotenv` (for managing environment variables)
* **APIs Used:**
    * [Google AI](https://ai.google.dev/)
    * [OpenWeather API](https://openweathermap.org/api)
    * [NewsAPI](https://newsapi.org/)
    * [SerpApi](https://serpapi.com/) (for Google Events)

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### 1. Prerequisites

* Python 3.8 or newer
* API keys for the following services:
    * [Google AI (Gemini)](https://makersuite.google.com/app/apikey)
    * [OpenWeather](https://home.openweathermap.org/api_keys)
    * [NewsAPI](https://newsapi.org/register)
    * [SerpApi](https://serpapi.com/manage-api-key)

### 2. Project Setup

**1. Clone the repository (Optional - or just create the files):**
```bash
git clone [https://github.com/your-username/morning-buddy.git](https://github.com/your-username/morning-buddy.git)
cd morning-buddy
````

**2. Create a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install dependencies:**
Create a `requirements.txt` file with the following content:

```
streamlit
google-generativeai
requests
python-dotenv
```

Install them using pip:

```bash
pip install -r requirements.txt
```

**4. Create the `.env` file:**
Create a file named `.env` in the root directory of the project. This file will store your secret API keys.

```ini
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
OPENWEATHER_API_KEY="YOUR_OPENWEATHER_API_KEY"
NEWS_API_KEY="YOUR_NEWS_API_KEY"
SERPAPI_API_KEY="YOUR_SERPAPI_API_KEY"
```

### 3\. File Structure

Your project should be organized as follows (based on the provided code):

```
morning-buddy/
├── applications.py   # Backend logic, API functions, Gemini calls
├── app.py            # Streamlit frontend UI and page routing
├── .env              # Stores all your secret API keys
├── requirements.txt  # Project dependencies
└── README.md         # You are here
```

  * `applications.py`: Contains all the backend logic, including API-calling functions (`get_weather`, `get_news`, `find_local_events`) and the Gemini-powered processing functions (`temperature_of_city`, `news_summarizer`, `smart_plan`).
  * `app.py`: Contains all the Streamlit code for the user interface, page routing, and custom CSS.

## Usage

Once your setup is complete, run the Streamlit application from your terminal:

```bash
streamlit run app.py
```

This will start the web server and open the "Morning Buddy" app in your default web browser. You can then navigate between the Home, Weather, News, and Planner pages using the sidebar.

## License

Distributed under the MIT License.

```
```
