from django.urls import path
from . import views
from appointments.views import book_appointment

urlpatterns = [
    path('book/', book_appointment, name='book_appointment'),
    path("book/success/<int:appointment_id>/", views.appointment_success, name="appointment_success"),
]