from django.urls import path
from main.views import *

app_name = 'main'



urlpatterns = [
    path("", index, name="index"),
    path("subject/", subject, name="subject"),
    path("practical/", practical, name="practical"),
    path("independent/", independent, name="independent"),
    path("presentation/", presentation, name="presentation"),
    path("video/", video, name="video"),
    path('venue_pdf/<int:pk>/', venue_pdf, name='venue_pdf')
]

