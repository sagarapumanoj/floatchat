# main.py
from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI(
    title="Ocean Data Monitoring API",
    description="Backend API for ocean data visualization and AI-driven insights",
    version="1.0.0"
)

# Root route
@app.get("/")
def root():
    return {"message": "Hello from FastAPI 🚀 - Ocean Data Monitoring API"}

# Example route: health check
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend is running fine!"}
