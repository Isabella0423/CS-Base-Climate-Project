from django.urls import URLPattern, path
from Temperature_by_City import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("AQI/<year>", views.annual_aqi, name="annual_aqi")
]