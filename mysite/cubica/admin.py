from django.contrib import admin

# Register your models here.
from .models import Post,Comment,Person,SubCube,Achievement

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Person)
admin.site.register(SubCube)
admin.site.register(Achievement)
