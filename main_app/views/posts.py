from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def detail(request, post_id):
    return render(request, 'posts/detail.html')
