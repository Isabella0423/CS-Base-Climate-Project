from xmlrpc.client import DateTime
from django.shortcuts import render

from django.http import HttpResponse
from pyowm.owm import OWM
from django.shortcuts import render
from datetime import datetime, timedelta


def home(request):
    owm = OWM('0aca60f9474adcfafed852266e956f71')
    airpollution = owm.airpollution_manager()
    start = datetime.strptime("2024/1/1", "%Y/%m/%d")
    end = datetime.strptime("2024/5/30", "%Y/%m/%d")
    list_of_historical_values = airpollution.air_quality_history_at_coords(51.507351, -0.127758, start, end=end)  # London, GB

    n=0
    totalaqi=0
    for air_status in list_of_historical_values:
        totalaqi=totalaqi+air_status.aqi
        n=n+1
    
    avergeaqi=totalaqi/n
    

    return HttpResponse("Average AQI for 2024 so far:"+str(avergeaqi))

def annual_aqi(request, year):
    owm = OWM('0aca60f9474adcfafed852266e956f71')
    airpollution = owm.airpollution_manager()
    t_start=str(year)+"/1/1"
    t_end=str(year)+"/12/31"
    print(t_start)
    print(t_end)
    start =datetime.strptime(t_start, "%Y/%m/%d")
    end= datetime.strptime(t_end,"%Y/%m/%d")
    list_of_historical_values = airpollution.air_quality_history_at_coords(51.507351, -0.127758, start, end=end)  # London, GB
    n=0
    totalaqi=0
    for air_status in list_of_historical_values:
        totalaqi=totalaqi+air_status.aqi
        n=n+1
    
    averageaqi=totalaqi/n
    
    return render(
        request,
        'Temperature_by_City/aqi_template.html',
        {
            'year' : year,
            'ave_aqi' : averageaqi
        }
    )