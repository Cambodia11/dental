from django.contrib import admin
from .models import Appointments
from django.contrib.admin import DateFieldListFilter

@admin.register(Appointments)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id","patient","doctor","date")
    list_filter = (("date",DateFieldListFilter),"doctor")
    search_fields = ("patient__first_name", "patient__last_name", "doctor__first_name", "doctor__last_name")

# Register your models here.
