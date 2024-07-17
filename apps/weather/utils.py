# Third-Party
import requests

# Django
from django.conf import settings

# Python
import logging


logger = logging.getLogger(__name__)


def format_response(data: dict):
    location = data.get("location")
    current = data.get("current")
    forecast: list[dict] = data["forecast"]["forecastday"]
    result = {}
    result["location"] = {
        "city": location["name"],
        "country": location["country"]
    }
    result["current"] = {
        "temp_c": current["temp_c"],
        "condition": current["condition"]["text"],
        "icon": f"https:{current["condition"]["icon"]}",
        "wind": current["wind_kph"],
        "humidity": current["humidity"]
    }
    for item in forecast:
        hours: list[dict] = item.get("hour")
        key = item.get("date")
        result[key] = {
            "sunrise": item["astro"]["sunrise"],
            "sunset": item["astro"]["sunset"]
        }
        for hour in hours:
            time = hour.get("time")
            result[key][time] = {
                "temp_c": hour["temp_c"],
                "condition": hour["condition"]["text"],
                "icon": f"https:{hour["condition"]["icon"]}",
                "wind": hour["wind_kph"],
                "humidity": hour["humidity"]
            }

    return result


def get_forecast(city: str, days: int = 0):
    url = settings.API_HOST+"/forecast.json"
    headers = {"key": settings.API_KEY}
    params = {"q": city, "lang": "ru"}
    if days > 0:
        params["days"] = days
    try:
        response = requests.get(url=url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return format_response(data=data)
    except requests.RequestException as e:
        logger.error(f"Request failed for get_forecast: {e}")
        return None
    