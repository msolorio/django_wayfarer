from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..models.City import City

@login_required
def index(request):
    profile = request.user.profile
    cities = City.objects.all()

    return render(request, 'cities/index.html', {
        'profile': profile,
        'cities': cities,
    })


@login_required
def detail(request, city_id):
    profile = request.user.profile
    cities = City.objects.all()
    selected_city = City.objects.get(id=city_id)

    return render(request, 'cities/detail.html', {
        'profile': profile,
        'cities': cities,
        'selected_city': selected_city,
    })
