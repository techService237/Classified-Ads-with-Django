from django.urls import path
from . import views

urlpatterns = [
    path('listing/', views.indexpage,name='listing'),
    path('form/',views.form,name='form'),
    path('details-ad/', views.detailsAd,name='details-ad'),

    ]

