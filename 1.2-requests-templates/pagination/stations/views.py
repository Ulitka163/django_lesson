from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    bus_stations = []
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_stations.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)
    bus_stations_page = paginator.page(page_number)
    context = {
        'bus_stations': bus_stations_page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
