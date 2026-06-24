import os
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="CareLink AI API Gateway",
    description="Main entry point for CareLink AI microservices",
    version="1.1.0"
)


AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service")
PATIENT_SERVICE_URL = os.getenv("PATIENT_SERVICE_URL", "http://patient-service")
APPOINTMENT_SERVICE_URL = os.getenv("APPOINTMENT_SERVICE_URL", "http://appointment-service")
NOTIFICATION_SERVICE_URL = os.getenv("NOTIFICATION_SERVICE_URL", "http://notification-service")
AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "http://ai-service")


class LoginRequest(BaseModel):
    username: str
    password: str


class NotificationRequest(BaseModel):
    recipient: str
    channel: str
    message: str


class TriageRequest(BaseModel):
    symptoms: str


class RiskScoreRequest(BaseModel):
    age: int
    condition: str
    blood_pressure_status: str


def call_service(url: str):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        raise HTTPException(
            status_code=503,
            detail=f"Service unavailable: {str(error)}"
        )


def post_to_service(url: str, payload: dict):
    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        raise HTTPException(
            status_code=503,
            detail=f"Service unavailable: {str(error)}"
        )


@app.get("/")
def root():
    return {
        "service": "CareLink AI API Gateway",
        "status": "running",
        "message": "Welcome to CareLink AI Platform"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "api-gateway",
        "version": "1.1.0"
    }


@app.get("/routes")
def service_routes():
    return {
        "routes": {
            "auth": "/auth/health, /auth/login",
            "patients": "/patients, /patients/{patient_id}",
            "appointments": "/appointments",
            "notifications": "/notifications, /notifications/send",
            "ai": "/ai/health, /ai/triage, /ai/risk-score",
            "platform": "/platform/health"
        }
    }


@app.get("/platform/health")
def platform_health():
    return {
        "api_gateway": {
            "status": "healthy",
            "service": "api-gateway"
        },
        "auth_service": call_service(f"{AUTH_SERVICE_URL}/health"),
        "patient_service": call_service(f"{PATIENT_SERVICE_URL}/health"),
        "appointment_service": call_service(f"{APPOINTMENT_SERVICE_URL}/health"),
        "notification_service": call_service(f"{NOTIFICATION_SERVICE_URL}/health"),
        "ai_service": call_service(f"{AI_SERVICE_URL}/health")
    }


@app.get("/auth/health")
def auth_health():
    return call_service(f"{AUTH_SERVICE_URL}/health")


@app.post("/auth/login")
def login(request: LoginRequest):
    return post_to_service(f"{AUTH_SERVICE_URL}/login", request.model_dump())


@app.get("/patients")
def list_patients():
    return call_service(f"{PATIENT_SERVICE_URL}/patients")


@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    return call_service(f"{PATIENT_SERVICE_URL}/patients/{patient_id}")


@app.get("/appointments")
def list_appointments():
    return call_service(f"{APPOINTMENT_SERVICE_URL}/appointments")


@app.get("/notifications")
def list_notifications():
    return call_service(f"{NOTIFICATION_SERVICE_URL}/notifications")


@app.post("/notifications/send")
def send_notification(request: NotificationRequest):
    return post_to_service(f"{NOTIFICATION_SERVICE_URL}/send", request.model_dump())


@app.get("/ai/health")
def ai_health():
    return call_service(f"{AI_SERVICE_URL}/health")


@app.post("/ai/triage")
def ai_triage(request: TriageRequest):
    return post_to_service(f"{AI_SERVICE_URL}/triage", request.model_dump())


@app.post("/ai/risk-score")
def ai_risk_score(request: RiskScoreRequest):
    return post_to_service(f"{AI_SERVICE_URL}/risk-score", request.model_dump())