from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Profile

@login_required
def my_profile(request):
    return redirect('profiles_detail', request.user.profile.id)

def detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    return render(request, 'profiles/detail.html', { 'profile': profile })

def update_profile_city(request):
    profile_id = request.POST['profile_id']
    selected_city_id = request.POST['selected_city_id']
    Profile.objects.filter(id=profile_id).update(city_id=selected_city_id)

    return redirect('cities_detail', selected_city_id)
