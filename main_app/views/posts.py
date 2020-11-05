from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import PostForm
from ..models import Post

@login_required
def detail(request, post_id):
    return render(request, 'posts/detail.html')

def create_post(request):
    post_form = PostForm(request.POST)

    if post_form.is_valid():
        city_id = request.POST['city']

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