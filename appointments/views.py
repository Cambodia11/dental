from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Appointments
from patients.models import Patient
from doctor.models import Doctor
from datetime import datetime
from django.utils import timezone
from django.contrib import messages

def book_appointment(request):
    if request.method == "POST":
        print(">>> POST пришёл:", request.POST)
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        phone = request.POST.get("phone", "").strip()
        doctor_id = request.POST.get("doctor")
        date = request.POST.get("date")
        time = request.POST.get("time")
        notes = request.POST.get("notes", "").strip()

        if not doctor_id:
            messages.error(request, "Пожалуйста, выберите врача.")
            return redirect("book_appointment")  # редирект вместо render

        doctor = get_object_or_404(Doctor, id=doctor_id)

        patient = Patient.objects.filter(
            phone=phone,
            first_name=first_name,
            last_name=last_name
        ).first()

        if not patient:
            # если такого пациента нет → создаём нового
            patient = Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone=phone
            )

        try:
            appointment_dt = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            if timezone.is_naive(appointment_dt):
                appointment_dt = timezone.make_aware(appointment_dt)
        except Exception:
            return render(request, "appointments/book_appointment.html", {
                "error": "Неверный формат даты/времени.",
            })

        appointment = Appointments.objects.create(
            patient=patient,
            doctor=doctor,
            date=appointment_dt,
            notes=notes
        )

        # после сохранения — редирект на страницу успеха
        return redirect(reverse("appointment_success", args=[appointment.id]))

    return render(request, "appointments/book_appointment.html")

def appointment_success(request, appointment_id):
    appointment = get_object_or_404(Appointments, id=appointment_id)
    return render(request, "appointments/success.html", {
        "first_name": appointment.patient.first_name,
        "date": appointment.date,   # <- оставляем datetime
        "time": appointment.date.strftime("%H:%M"),
        "doctor": str(appointment.doctor),
    })