from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="CareLink AI Service",
    description="AI-powered triage and risk scoring service for CareLink AI Platform",
    version="1.0.0"
)


class TriageRequest(BaseModel):
    symptoms: str


class RiskScoreRequest(BaseModel):
    age: int
    condition: str
    blood_pressure_status: str


@app.get("/")
def root():
    return {
        "service": "CareLink AI Service",
        "status": "running",
        "message": "AI Service is available"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ai-service"
    }


@app.post("/triage")
def triage(request: TriageRequest):
    symptoms = request.symptoms.lower()

    if "chest pain" in symptoms or "shortness of breath" in symptoms:
        recommendation = "Seek urgent medical attention."
        priority = "high"
    elif "fever" in symptoms or "headache" in symptoms:
        recommendation = "Book a consultation with a healthcare provider."
        priority = "medium"
    else:
        recommendation = "Monitor symptoms and consult a doctor if they persist."
        priority = "low"

    return {
        "symptoms": request.symptoms,
        "priority": priority,
        "recommendation": recommendation,
        "disclaimer": "This is a simulated AI response for DevOps demonstration only."
    }


@app.post("/risk-score")
def risk_score(request: RiskScoreRequest):
    score = 0

    if request.age >= 60:
        score += 2
    elif request.age >= 40:
        score += 1

    if request.condition.lower() in ["diabetes", "hypertension"]:
        score += 2

    if request.blood_pressure_status.lower() == "high":
        score += 2

    if score >= 5:
        risk = "high"
    elif score >= 3:
        risk = "medium"
    else:
        risk = "low"

    return {
        "age": request.age,
        "condition": request.condition,
        "blood_pressure_status": request.blood_pressure_status,
        "risk_level": risk,
        "score": score,
        "disclaimer": "This is a mock risk score for platform demonstration only."
    }