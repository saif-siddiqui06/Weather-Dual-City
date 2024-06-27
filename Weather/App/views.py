from django.shortcuts import render , HttpResponse ,redirect
import urllib.request
import requests
import json
import datetime

# Create your views here.

def Home(request):
     return render(request, 'index.html')


def HomePage(request):
     if request.method == 'POST':
          city = request.POST.get('city1')
          city2 = request.POST.get('city2')
          print(city)
          
     key = '3ca6c3f24409cd40aef96a30cd41031c'
     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3ca6c3f24409cd40aef96a30cd41031c'
     forcaste = 'http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid=3ca6c3f24409cd40aef96a30cd41031c'
     
     if request.method == 'POST':
     
          city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
          city_weather2 = requests.get(url.format(city2)).json() #request the API data and convert the JSON to Python data types

          lat,lon = city_weather['coord']['lat'], city_weather['coord']['lon']
          forcaste_result = requests.get(forcaste.format(lat,lon,)).json()
          
          weather = {
          'city' : city,
          'temperature' : round((city_weather['main']['temp'] - 32) * (5/9),2),
          'Feellikes' : round((city_weather['main']['feels_like'] - 32) * (5/9),2),

          'description' : city_weather['weather'][0]['description'],
          'humidity' : city_weather['main']['humidity'],
          'pressure' : city_weather['main']['pressure'],
          'wind' : city_weather['wind']['speed'],
          'icon' : city_weather['weather'][0]['icon']
          }
          
          weather2 = {
          'city' : city2,
          'temperature' : round((city_weather2['main']['temp'] - 32) * (5/9),2),
          'Feellikes' : round((city_weather2['main']['feels_like'] - 32) * (5/9),2),

          'description' : city_weather2['weather'][0]['description'],
          'humidity' : city_weather2['main']['humidity'],
          'pressure' : city_weather2['main']['pressure'],
          'wind' : city_weather2['wind']['speed'],
          'icon' : city_weather2['weather'][0]['icon']
          }
          
          print(forcaste_result)
          
          context = {'weather' : weather,
                     'weather2' : weather2,}
          
          print(city_weather)
          print(city2)
          print(city_weather2)
          
          
          return render(request,'index.html',context)
     
     else :
          return render(request,'index.html')