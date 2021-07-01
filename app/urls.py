from django.urls import path

from .views import *

app_name = "main_app"

urlpatterns = [
    path('', HomePageView.as_view(), name="homepage"),
    path('blog/<str:slug>/', DetailViews.as_view(), name='detailview'),
    path('categories/<str:slug>/', CategoriesView.as_view(), name='categories'),
    path('region/<slug:slug>/', RegionView.as_view(), name='region'),
    path('hash/<slug:slug>/', HashtagsView.as_view(), name='hashtag'),
]
