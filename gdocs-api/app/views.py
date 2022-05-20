
# python -m venv venv
# source env/bin/activate
# pip install django
# pip install gspread
# django-admin startproject project .
# python manage.py startapp app

# Em project/settings.py adicionar 'app' ao final da lista INSTALLED_APPS
# Em project/urls.py adicionar from app.views import home
# E adcicionar na lista urlpatterns: path('', home)

# python manage.py runserver

from django.shortcuts import render
from django.http import HttpResponse
import gspread

gc = gspread.service_account(filename='.service_account.json')
sh = gc.open_by_key('1Ise8zJkIX91XAnEBVrduFuha2kWdYqjuVdbOnvQGAh8')


# Create your views here
def home(request):
    worksheet = sh.worksheet('Página1')
    return HttpResponse(worksheet.acell('B3').value)

