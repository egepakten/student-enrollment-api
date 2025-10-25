"""
Student Enrollment API
Simple FastAPI application for CI/CD learning
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import os
from datetime import datetime

app = FastAPI(
    title="Student Enrollment API",
    version="1.0.0",
    description="Simple FastAPI application for CI/CD learning",
)

# Simple in-memory storage (in real app, this would be DynamoDB)
enrollments = []

class EnrollmentRequest(BaseModel):
    student_id: str
    course_id: str
    student_name: str

class EnrollmentResponse(BaseModel):
    success: bool
    enrollment_id: Optional[str] = None
    message: str
    timestamp: str
    version: str

@app.get("/")
def root():
    """ Health check endpoint """
    return {
        "status":"healthy",
        "service":"Student Enrollment API",
        "version":"1.0.0",
        "environment":os.getenv("ENVIRONMENT", "development")
    }

@app.get("/health")
def health_check():
    """ Health Check Endpoint for ALB/API Gateway """
    return {
        "status":"healthy",
        "timestamp":datetime.utcnow().isoformat()
    }

@app.post("/enroll", response_model=EnrollmentResponse)
def enroll_student(request:EnrollmentRequest):
    """ Enroll a student in a course
    
    This endpoint demonstrates:
    - Request validation
    - Error handling
    - Response formatting
    """
    try:
        # Simple Validation
        if not request.student_id or not request.course_id:
            raise HTTPException(status_code=400,detail="student_id and course_id are required")
        
        # Create enrollment
        enrollment_id = f"ENR-{len(enrollments)+1:04d}"
        enrollment = {
            "id":enrollment_id,
            "student_id":request.student_id,
            "course_id":request.course_id,
            "student_name":request.student_name,
            "timestamp":datetime.utcnow().isoformat()
        }
        enrollments.append(enrollment)
        return EnrollmentResponse(success=True,enrollment_id=enrollment_id,message=f"Successfully enrolled {request.student_name} in course {request.course_id}",timestamp=datetime.utcnow().isoformat(),version="1.0.0")
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

@app.get("/enrollments")
def get_enrollments():
    """Get all enrollments (for testing)"""
    return {
        "total": len(enrollments),
        "enrollments": enrollments
    }

# For Lambda handler
def lambda_handler(event, context):
    """
    AWS Lambda handler
    This allows the same FastAPI app to run on Lambda
    """
    from mangum import Mangum
    handler = Mangum(app)
    return handler(event, context)