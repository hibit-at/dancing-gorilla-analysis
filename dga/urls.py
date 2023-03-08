from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("analyze_replay/", views.analyze_replay),
    path("registration/", views.registration, name="registration"),
    path('result/', views.result, name='result'),
    path('qa/', views.qa, name='qa')
]