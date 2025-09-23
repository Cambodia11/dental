from django.contrib import admin
from.models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone", "birth_date", "created_at")
    search_fields = ("first_name", "last_name", "phone")
    ordering = ("-created_at",)
    list_editable = ("phone",)
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Основная информация", {"fields": ("first_name", "last_name", "phone")}),
        ("Дополнительно", {"fields": ("birth_date", "created_at")}),
    )

# Register your models here.
