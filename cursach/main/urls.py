from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('Kino', views.steps, name='steps'),
    path('Kino/persons', views.persons, name='persons'),
    path('DomainChecker', views.steps, name='steps'),
    path('DomainChecker/persons', views.persons, name='persons'),
    #Сделать автодописывание двух новых строчек проекта

]