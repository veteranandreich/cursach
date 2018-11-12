from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('auth', views.auth, name='auth'),
    path('steps', views.steps, name='steps'),
    path('persons', views.persons, name='persons'),
    path('personsinfo', views.personsinfo, name='personsinfo'),
    path('stepsinfo', views.stepsinfo, name='stepssinfo'),
    path('addperson', views.addperson, name='addperson'),
    path('addadmin', views.addadmin, name='addadmin'),
    path('addstep', views.addstep, name='addstep'),
    path('addproject', views.addproject, name='addproject'),
    path('editstep', views.editstep, name='editstep'),

]