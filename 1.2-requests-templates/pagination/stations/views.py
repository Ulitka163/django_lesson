from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


bus_stations_ = []
with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        bus_stations_.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations_, 10)
    page = paginator.page(page_number)
    bus_stations_page = page.object_list
    context = {
        'bus_stations': bus_stations_page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
