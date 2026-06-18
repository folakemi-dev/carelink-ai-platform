from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="CareLink AI Patient Service",
    description="Patient records service for CareLink AI Platform",
    version="1.0.0"
)


patients = [
    {
        "id": 1,
        "name": "Amina Yusuf",
        "age": 34,
        "condition": "Hypertension",
        "status": "stable"
    },
    {
        "id": 2,
        "name": "David Okafor",
        "age": 42,
        "condition": "Diabetes",
        "status": "monitoring"
    }
]


@app.get("/")
def root():
    return {
        "service": "CareLink AI Patient Service",
        "status": "running",
        "message": "Patient Service is available"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "patient-service"
    }


@app.get("/patients")
def list_patients():
    return {
        "count": len(patients),
        "patients": patients
    }


@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient

    raise HTTPException(status_code=404, detail="Patient not found")