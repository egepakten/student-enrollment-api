"""
Unit tests for Student Enrollment API
These tests will run in CodeBuild pipeline
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    """ Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "version" in response.json()

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_enroll_student_success():
    """Test successful student enrollment"""
    enrollment_data = {
        "student_id": "STU001",
        "course_id": "AWS101",
        "student_name": "John Doe"
    }
    
    response = client.post("/enroll", json=enrollment_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["success"] == True
    assert "enrollment_id" in data
    assert "John Doe" in data["message"]

def test_enroll_student_missing_fields():
    """Test enrollment with missing fields"""
    enrollment_data = {
        "student_id": "",
        "course_id": "AWS101",
        "student_name": "John Doe"
    }
    
    response = client.post("/enroll", json=enrollment_data)
    assert response.status_code == 400

def test_get_enrollments():
    """Test getting all enrollments"""
    response = client.get("/enrollments")
    assert response.status_code == 200
    assert "total" in response.json()
    assert "enrollments" in response.json()