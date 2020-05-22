from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('wrongdoc/',view.index),
]
