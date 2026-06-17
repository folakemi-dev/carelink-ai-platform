from fastapi import FastAPI

app = FastAPI(
    title="CareLink AI API Gateway",
    description="Main entry point for CareLink AI microservices",
    version="1.0.0"
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
        "service": "api-gateway"
    }


@app.get("/routes")
def service_routes():
    return {
        "available_services": [
            "auth-service",
            "patient-service",
            "appointment-service",
            "notification-service",
            "ai-service"
        ]
    }