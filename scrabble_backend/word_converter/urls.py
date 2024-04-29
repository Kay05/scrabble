from django.urls import path

from .views import convert_sentence

urlpatterns = [
    path('', convert_sentence, name='convert_sentence'),
]