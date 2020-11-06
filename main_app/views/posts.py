from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import PostForm
from ..models import Post, City

@login_required
def detail(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'posts/detail.html', { 'post': post })


def create_post(request, city_id):
    selected_city = City.objects.get(id=city_id)
    profile = request.user.profile
    post_form = PostForm()

    return render(request, 'posts/create_post.html', {
        'selected_city': selected_city,
        'post_form': post_form,
    })


def add_post(request, city_id):
    post_form = PostForm(request.POST)

    if post_form.is_valid():
        Post.objects.create(
            author_id=request.POST['author'],
            city_id=city_id,
            title=request.POST['title'],
            body=request.POST['body']
        )

        return redirect('cities_detail', city_id)

        # Option 2 for saving a post
        # savable_form = post_form.save(commit=False)
        # savable_form.author_id = request.POST['author']
        # savable_form.city_id = request.POST['city']
        # savable_form.save()