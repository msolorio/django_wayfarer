from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def detail(request):
    return render(request, 'profiles/detail.html')
