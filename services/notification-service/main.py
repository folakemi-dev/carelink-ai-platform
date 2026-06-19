from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="CareLink AI Notification Service",
    description="Notification service for CareLink AI Platform",
    version="1.0.0"
)


class NotificationRequest(BaseModel):
    recipient: str
    channel: str
    message: str


notifications = [
    {
        "id": 1,
        "recipient": "amina.yusuf@example.com",
        "channel": "email",
        "message": "Your appointment has been scheduled.",
        "status": "sent"
    }
]


@app.get("/")
def root():
    return {
        "service": "CareLink AI Notification Service",
        "status": "running",
        "message": "Notification Service is available"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "notification-service"
    }


@app.get("/notifications")
def list_notifications():
    return {
        "count": len(notifications),
        "notifications": notifications
    }


@app.post("/send")
def send_notification(request: NotificationRequest):
    new_notification = {
        "id": len(notifications) + 1,
        "recipient": request.recipient,
        "channel": request.channel,
        "message": request.message,
        "status": "sent"
    }

    notifications.append(new_notification)

    return {
        "message": "Notification sent successfully",
        "notification": new_notification
    }