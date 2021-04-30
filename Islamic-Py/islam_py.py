import json
import requests
import datetime

date_now = datetime.datetime.now()

class islam():
    
    def time(country,city,method=None,mode=None):

        querystring = {
            "country":country,"year":date_now.year,"month":date_now.month,"city":city,"method":method}
        headers = {
            'x-rapidapi-key': "b281e6a2eamshf5db96c85f9a12cp1dcadajsn3cca41194cc8",
            'x-rapidapi-host': "aladhan.p.rapidapi.com"
            }
        response = requests.request("GET", "https://aladhan.p.rapidapi.com/calendarByCity", headers=headers, params=querystring)
        data = response.text
        json_data = json.loads(data)
        timings = json_data["data"][date_now.day - 1]["timings"]
        if mode is None:
            pass
        elif mode == "Fajr":
            return timings["Fajr"]
        elif mode == "Sunrise":
            return timings["Sunrise"]
        elif mode == "Dhuhr":
            return timings["Dhuhr"]
        elif mode == "Asr":
            return timings["Asr"]
        elif mode == "Sunset":
            return timings["Sunset"]
        elif mode == "Maghrib":
            return timings["Maghrib"]
        elif mode == "Isha":
            return timings["Isha"]
        elif mode == "Imsak":
            return timings["Imsak"]
        elif mode == "Midnight":
            return timings["Midnight"]


    def hijri(country,city):
        querystring = {
            "country":country,"year":date_now.year,"month":date_now.month,"city":city}
        headers = {
            'x-rapidapi-key': "b281e6a2eamshf5db96c85f9a12cp1dcadajsn3cca41194cc8",
            'x-rapidapi-host': "aladhan.p.rapidapi.com"
            }
        response = requests.request("GET", "https://aladhan.p.rapidapi.com/calendarByCity", headers=headers, params=querystring)
        data = response.text
        json_data = json.loads(data)
        date = json_data["data"][date_now.day - 1]["date"]["hijri"]["date"]
        return date
