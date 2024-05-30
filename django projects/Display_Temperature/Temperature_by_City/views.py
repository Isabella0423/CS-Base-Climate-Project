from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from pyowm.owm import OWM
#from pyowm.utils import config
#from pyowm.utils import timestamps


def home(request):
    owm = OWM('0aca60f9474adcfafed852266e956f71')
    manager = owm.weather_manager()
    #station_id = 39276
    #historian = manager.station_tick_history(station_id, limit=4)
    return HttpResponse("This is temperature: ", historian.temperature_series(unit="celsius"))