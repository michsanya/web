from django.shortcuts import render
from django.http import HttpResponse
from .models import Station
from django.template import loader


# Create your views here.
def index(request):
    station_list = Station.objects.order_by('name')[:2]
    template = loader.get_template('Station/index.html')
    context = {
        'station_list': station_list,
    }
    return render(request, 'Station/index.html' ,context, )

def detail(request, station_id):
    return HttpResponse("You are looking for station # %s" % station_id)
