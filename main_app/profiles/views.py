from django.shortcuts import render

def detail(request, profile_id):
    return render(request, 'profiles/detail.html')
