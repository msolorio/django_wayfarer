from django.contrib import admin
from .models import City
from .models import Profile
from .models import Post

admin.site.register(City)
admin.site.register(Profile)
admin.site.register(Post)
