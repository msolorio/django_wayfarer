from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..models import City, Post
from ..forms import PostForm

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
    posts = Post.objects.filter(city_id=city_id)

    post_form = PostForm()

    return render(request, 'cities/detail.html', {
        'profile': profile,
        'cities': cities,
        'selected_city': selected_city,
        'selected_city_fullname': f'{selected_city.name}, {selected_city.country}',
        'post_form': post_form,
        'posts': posts
    })
