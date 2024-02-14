from django.shortcuts import render
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

API_KEY = 'api_key...'

class WeatherAPIView(APIView):
    def get(self, request):
        if 'location' in request.GET:
            location = request.GET['location']
            url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return render(request, 'weather.html', {'data': data})
            else:
                return render(request, 'weather.html',{'error':'Please Enter a Valid City Name Sir..','query_name':location})
        else:
            return render(request, 'weather.html')