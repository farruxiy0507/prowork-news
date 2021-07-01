from django.views.generic import ListView, DetailView

from .models import *


class HomePageView(ListView):
    template_name = 'index.html'
    queryset = Blog.objects.order_by('-created_at')


class DetailViews(DetailView):
    model = Blog
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailViews, self).get_context_data(**kwargs)
        return context


class CategoriesView(ListView):
    template_name = 'hashtag.html'
    model = Blog

    def get_queryset(self):
        queryset = self.model.objects.filter(category__slug=self.kwargs.get('slug'))
        return queryset


class RegionView(ListView):
    model = Blog
    template_name = 'hashtag.html'

    def get_queryset(self):
        return Blog.objects.filter(region__slug=self.kwargs.get('slug'))


class HashtagsView(ListView):
    model = Blog
    template_name = 'hashtag.html'

    def get_queryset(self):
        return Blog.objects.filter(hashtag__slug=self.kwargs.get('slug'))