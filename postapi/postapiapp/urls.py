from django.urls import path
from . import views

urlpatterns=[
    path('Person/',views.PersonView.as_view(),name='Person'),
    path('Personupdate/<int:pk>/',views.PersonViewUpdate.as_view(),name='Personupdate')
]