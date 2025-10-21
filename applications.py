import requests.exceptions
from dotenv import load_dotenv
import os
import google.generativeai as genai
from google.generativeai import types

import requests
import datetime

# Load environment variables
load_dotenv()

# Load all API keys from .env
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# Validate keys
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found ")
if not OPENWEATHER_API_KEY:
    raise ValueError("OPENWEATHER_API_KEY not found ")
if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY not found")
if not SERPAPI_API_KEY:
    raise ValueError("SERPAPI_API_KEY not found")

# Initialize Gemini Client
client = genai.Client(api_key=GOOGLE_API_KEY)


# FUNCTION TO GET WEATHER OF A CITY.
def get_weather(city: str):
    """Fetches current weather for a given city using API"""
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# GEMINI CODE TO USE THE FUNCTION TO GET DETAILS OF THE CITY
def temperature_of_city(city):
    system_instructions = """
You are a professional weather assistant that converts raw JSON weather data 
(from the OpenWeather API) into a clear, natural, and accurate weather report.

Formatting and style rules:
1. Always begin with: “Here’s the weather update for <city>, <country>:”
2. Convert all temperatures from Kelvin to Celsius (°C), rounded to 1 decimal place.
3. Report the following details clearly and in this order:
   - Weather condition (e.g., Clear sky, Light rain, Hazy, etc.)
   - Temperature and feels-like temperature in °C
   - Humidity (%)
   - Wind speed (m/s)
   - Sunrise and sunset times in local time (IST), formatted as “HH:MM AM/PM”
4. Keep the tone friendly, human-like, and concise — as if explaining to a traveler.
5. Add a helpful suggestion based on the conditions, such as:
   - If hot: “Stay hydrated and wear light clothes.”
   - If rainy: “Carry an umbrella.”
   - If cold: “Wear something warm.”
6. Use plain English sentences (no bullet points unless describing data).
7. If any field is missing, ignore it gracefully without mentioning the absence.
8. The final response should be under 120 words and sound natural, not robotic.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Generate a clear, friendly weather report for {city}.",
        config=types.GenerateContentConfig(
            system_instruction=system_instructions,
            tools=[get_weather],
        ),
    )
    return response.candidates[0].content.parts[0].text


# FUNCTION TO GET NEWS OF INTEREST
def get_news(topic: str):
    """Fetches latest news headlines from an API"""
    try:
        url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}&pageSize=5&sortBy=publishedAt"
        response = requests.get(url)
        return response.json().get("articles", [])
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# FUNCTION TO SUMMARIZE THE NEWS
def news_summarizer(url):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"summarize news from the url:- {url}",
    )
    return response.text


# FUNCTION TO GET FORECAST OF ENTIRE DAY FOR A CITY AND PLACES TO VISIT
def get_forcasted_weather(city: str):
    """Fetches forecasted weather and tourist places to visit for a city."""
    try:
        grounding_tool = types.Tool(google_search=types.GoogleSearch())
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=f"""
            Provide detailed weather forecast for {city} on {datetime.date.today()}.
            Also list top recommended places to visit in {city} today.
            """,
            config=types.GenerateContentConfig(tools=[grounding_tool]),
        )
        return response.text
    except Exception as e:
        return {"error": str(e)}


# FUNCTION TO FIND LOCAL EVENTS
def find_local_events(city: str):
    """Finds local events for a given city using an API."""
    try:
        url = f"https://serpapi.com/search.json?engine=google_events&q=Events in {city}&api_key={SERPAPI_API_KEY}"
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# FUNCTION FOR SMART PLANNER
def smart_plan(city):
    prompt = f"""
    You are a smart travel and event planner assistant.
    Your job is to create a personalized day itinerary for the user in a given {city}.
    Include weather, events, and places to visit. Keep tone friendly and actionable.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[find_local_events, get_forcasted_weather]
        ),
    )
    return response.candidates[0].content.parts[0].text


# MAIN EXECUTION
if __name__ == "__main__":
    abc = smart_plan("delhi")
    print(abc)

