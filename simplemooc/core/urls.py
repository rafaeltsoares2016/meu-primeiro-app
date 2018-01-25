
from django.urls import include, path

from simplemooc.core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
]