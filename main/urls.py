from django.urls import path
from . import views
from appointments.views import book_appointment

urlpatterns = [
    path('', views.home, name='home'),
]