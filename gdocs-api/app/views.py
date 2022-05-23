# Links úteis
# developers.google.com/sheets/api/quickstart/python
# docs.gspread.org/en/latest/
# console.cloud.google.com/apis/

# python -m venv venv
# source venv/bin/activate
# pip install django
# pip install gspread
# django-admin startproject project .
# python manage.py startapp app

# Em project/settings.py adicionar 'app' ao final da lista INSTALLED_APPS
# Em project/urls.py adicionar from app.views import home
# E adicicionar na lista urlpatterns: path('', home)

# python manage.py runserver

from django.shortcuts import render
from django.http import HttpResponse
import gspread

gc = gspread.service_account(filename='.service_account.json')
sh = gc.open_by_key('1Ise8zJkIX91XAnEBVrduFuha2kWdYqjuVdbOnvQGAh8')


# Create your views here
def home(request):
    worksheet = sh.worksheet('Página1')
    while True:
        #search = input('Insira a célula a ser pesquisada: ')
        update = input('Insira a célula a ser substituída: ')
        worksheet.update(update, "teste")
        return HttpResponse(worksheet.acell(update).value)

