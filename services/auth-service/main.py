from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="CareLink AI Auth Service",
    description="Authentication service for CareLink AI Platform",
    version="1.0.0"
)


class LoginRequest(BaseModel):
    username: str
    password: str


@app.get("/")
def root():
    return {
        "service": "CareLink AI Auth Service",
        "status": "running",
        "message": "Auth Service is available"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "auth-service"
    }


@app.post("/login")
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "password":
        return {
            "status": "success",
            "message": "Login successful",
            "token": "mock-jwt-token"
        }

    return {
        "status": "failed",
        "message": "Invalid username or password"
    }


@app.get("/validate")
def validate_token():
    return {
        "status": "valid",
        "message": "Token validation endpoint is working"
    }