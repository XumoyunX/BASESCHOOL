from django.urls import path
from main.views import *

app_name = 'main'



urlpatterns = [
    path("", index, name="index"),
    path("subject_url/", subject, name="subject_url"),
    path("practical/", practical, name="practical"),
    path("independent/", independent, name="independent"),
    path("presentation/", presentation, name="presentation"),
    path("video/", video, name="video"),
    path('pdf/', pdf, name='pdf'),
    path('tests/', test_list, name='test_list'),
    path('tests/<int:id>/', start_test, name='start_test'),
    path('tests/<int:id>/submit/', submit_test, name='submit_test'),
]

