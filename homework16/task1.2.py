import requests
import statistics
import threading
import multiprocessing
import time
import json

def average_weather(temperature):
    c = statistics.mean(temperature)
    print(round(c))
    d = (round(c))
def weather():
    lst = []
    K_url = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={"latitude": 50.45,
                "longitude":30.52,
                "hourly": "temperature_2m"
                }
    )
    K_temperature = K_url.json()["hourly"]["temperature_2m"]
    RT_url = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={"latitude": 51.92,
                  "longitude": 4.48,
                  "hourly": "temperature_2m"
              }
    )
    RT_temperature = RT_url.json()["hourly"]["temperature_2m"]
    P_url = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={"latitude": 49.59,
                  "longitude": 34.55,
                  "hourly": "temperature_2m"
              }
    )
    P_temperature = P_url.json()["hourly"]["temperature_2m"]
    D_url = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={"latitude": 48.47,
                "longitude": 35.04,
                "hourly": "temperature_2m"
              }
    )
    D_temperature = D_url.json()["hourly"]["temperature_2m"]
    KM_url = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={"latitude": 48.70,
                "longitude": 26.61,
                "hourly": "temperature_2m"
              }
    )
    KM_temperature = KM_url.json()["hourly"]["temperature_2m"]
    multiprocessing()
    print(f"it's hotter right now: {max(lst)}")
@average_weather
def multiprocessing():

    (multiprocessing.Process(target=average_weather, args=(K_temperature,)))
    (multiprocessing.Process(target=average_weather, args=(RT_temperature,)))
    (multiprocessing.Process(target=average_weather, args=(P_temperature,)))
    (multiprocessing.Process(target=average_weather, args=(D_temperature,)))
    (multiprocessing.Process(target=average_weather, args=(KM_temperature,)))
    print(time.time())
    lst.append(statistics.mean(K_temperature))
    lst.append(statistics.mean(RT_temperature))
    lst.append(statistics.mean(P_temperature))
    lst.append(statistics.mean(D_temperature))
    lst.append(statistics.mean(KM_temperature))


weather()