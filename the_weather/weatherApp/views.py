from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5c0b4fa1ce73479bec7a8a2ad50381f5'

    if request.method =='POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities=City.objects.all()
    weather_data =[]
    for city in cities:
        r= requests.get(url.format(city)).json()

        city_weather={
            'city':city.name,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],

        }
        weather_data.append(city_weather)

    context ={'weather_data':weather_data, 'form':form}
    return render(request,'weatherApp/index.html',context)


'''
{"coord":{"lon":85.9,"lat":26.16},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"base":"stations","main":{"temp":93.77,"pressure":997.82,"humidity":56
,"temp_min":93.77,"temp_max":93.77,"sea_level":997.82,"grnd_level":992.03},"wind":{"speed":5.7,"deg":167.308},"clouds":{"all":79},"dt":1566469902,"sys":{"message":0.0069,"country":"IN","
sunrise":1566431517,"sunset":1566478040},"timezone":19800,"id":1273491,"name":"Darbhanga","cod":200}
'''