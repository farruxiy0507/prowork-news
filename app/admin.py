from django.contrib import admin
from parler.admin import TranslatableAdmin

from .forms import BlogForm
from .models import Category, Regions, Blog, Hashtags, PicturesFromTheBlog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Regions)
class RegiosnsAdmin(TranslatableAdmin):
    list_display = ('name',)



@admin.register(Blog)
class BlogAdmin(TranslatableAdmin):
    list_display = ('title', 'category')
    form = BlogForm


@admin.register(Hashtags)
class HashtagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PicturesFromTheBlog)
class PicturesAdmin(admin.ModelAdmin):                                                                                                                                                                                                  
    list_display = ('owner',)
