from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Profile
from ..forms import ProfileForm

# @login_required
# def my_profile(request):
#     return redirect('profiles_detail', 'my_profile')

@login_required
def detail(request, profile_id):

    if profile_id == 0:
        profile = request.user.profile
    else:
        profile = Profile.objects.get(id=profile_id)

    return render(request, 'profiles/detail.html', { 'profile': profile })

@login_required
def edit(request):
    profile = request.user.profile

    profile_form = ProfileForm({
        'city': profile.city,
        'email': profile.email,
        'img_url': profile.img_url,
        'bio': profile.bio,
    })

    return render(request, 'profiles/edit.html', {
        'profile': profile,
        'profile_form': profile_form,
    })


def update(request):
    profile_id = request.user.profile.id
    profile_form = ProfileForm(request.POST)

    if profile_form.is_valid():
        Profile.objects.filter(id=profile_id).update(
            city_id=request.POST['city'],
            email=request.POST['email'],
            img_url=request.POST['img_url'],
            bio=request.POST['bio'],
        )

    return redirect('profiles_edit')


def profiles_update_city(request):
    profile_id = request.POST['profile_id']
    selected_city_id = request.POST['selected_city_id']
    Profile.objects.filter(id=profile_id).update(city_id=selected_city_id)

    return redirect('cities_detail', selected_city_id)
