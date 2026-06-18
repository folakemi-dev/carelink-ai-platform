from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="CareLink AI Appointment Service",
    description="Appointment management service for CareLink AI Platform",
    version="1.0.0"
)


class AppointmentRequest(BaseModel):
    patient_id: int
    doctor: str
    date: str
    time: str
    reason: str


appointments = [
    {
        "id": 1,
        "patient_id": 1,
        "doctor": "Dr. Sarah Bello",
        "date": "2026-06-20",
        "time": "10:00",
        "reason": "Blood pressure review",
        "status": "scheduled"
    },
    {
        "id": 2,
        "patient_id": 2,
        "doctor": "Dr. James Adeyemi",
        "date": "2026-06-21",
        "time": "14:30",
        "reason": "Diabetes follow-up",
        "status": "scheduled"
    }
]


@app.get("/")
def root():
    return {
        "service": "CareLink AI Appointment Service",
        "status": "running",
        "message": "Appointment Service is available"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "appointment-service"
    }


@app.get("/appointments")
def list_appointments():
    return {
        "count": len(appointments),
        "appointments": appointments
    }


@app.get("/appointments/{appointment_id}")
def get_appointment(appointment_id: int):
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            return appointment

    raise HTTPException(status_code=404, detail="Appointment not found")


@app.post("/appointments")
def create_appointment(request: AppointmentRequest):
    new_appointment = {
        "id": len(appointments) + 1,
        "patient_id": request.patient_id,
        "doctor": request.doctor,
        "date": request.date,
        "time": request.time,
        "reason": request.reason,
        "status": "scheduled"
    }

    appointments.append(new_appointment)

    return {
        "message": "Appointment created successfully",
        "appointment": new_appointment
    }