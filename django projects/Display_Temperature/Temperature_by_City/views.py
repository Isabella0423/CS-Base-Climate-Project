from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from pyowm.owm import OWM
#from pyowm.utils import config
#from pyowm.utils import timestamps


def home(request):
    owm = OWM('0aca60f9474adcfafed852266e956f71')
    airpollution = owm.airpollution_manager()
    start = 1606223802  # November 24, 2020
    # ...or fetch history on a closed timeframe in the past
    end = 1613864065  # February 20, 2021
    list_of_historical_values = airpollution.air_quality_history_at_coords(51.507351, -0.127758, start, end=end)  # London, GB

    # Each item in the list_of_historical_values is an AirStatus object 
    n=0
    totalaqi=0
    for air_status in list_of_historical_values:
        #air_status.co
        #air_status.no
        #air_status.no2
        #air_status.o3
        #air_status.so2
        #air_status.pm2_5
        #air_status.pm10
        #air_status.nh3
        print(air_status.aqi)  # air quality index
        totalaqi=totalaqi+air_status.aqi
        n=n+1
    
    avergeaqi=totalaqi/n
    #mgr2=owm.weather_manager()
    #manager = owm.weather_manager()
    #station_id = 39276
    #historian = manager.station_tick_history(station_id, limit=4)
    
    place= "Toronto"
    start_date= "1985-01-01"
    end_date="1985-12-31"
    #history = manager.weather_history_at_place(place, start_date, end_date)
    #history_list = history.get_weathers()
    #for weather in history_list:
    #    temperature = weather.get_temperature('celsius') 
    #   print(f'Temperature: {temperature}°C')
        



    #print(historian.temperature_series(unit="celsius"))

    return HttpResponse("Average AQI:"+str(avergeaqi))