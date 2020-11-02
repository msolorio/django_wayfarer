from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def detail(request):
    profile = request.user.profile
    user = request.user

    return render(request, 'profiles/detail.html', {
        'profile': profile,
        'user': user,
        'current_city': profile.city or 'Current City Not Selected'
    })
