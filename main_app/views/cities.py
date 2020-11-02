from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    print(request.user)

    return render(request, 'cities/index.html')


@login_required
def detail(request, city_id):
    return render(request, 'cities/detail.html')
