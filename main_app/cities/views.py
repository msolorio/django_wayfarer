from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'cities/index.html')


def detail(request, city_id):
    return render(request, 'cities/detail.html')
