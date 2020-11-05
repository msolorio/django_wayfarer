from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Profile

@login_required
def detail(request):
    profile = request.user.profile
    user = request.user

    return render(request, 'profiles/detail.html', {
        'profile': profile,
        'user': user,
        'current_city': profile.city or 'Current City Not Selected'
    })

def update_profile_city(request):
    profile_id = request.POST['profile_id']
    selected_city_id = request.POST['selected_city_id']
    Profile.objects.filter(id=profile_id).update(city_id=selected_city_id)

    return redirect('cities_detail', selected_city_id)
