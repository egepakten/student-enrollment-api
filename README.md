# 🎓 Student Enrollment API - AWS CI/CD Pipeline

A production-ready FastAPI application demonstrating complete AWS CI/CD automation with multiple deployment strategies.

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)
![AWS](https://img.shields.io/badge/AWS-CI%2FCD-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🚀 Project Overview

This project demonstrates enterprise-grade CI/CD practices using AWS services:

- **Automated Testing** with pytest in AWS CodeBuild
- **Containerization** with Docker and Amazon ECR
- **Dual Deployment Strategies**:
  - 🔵 Lambda + API Gateway (Canary deployment)
  - 🟢 ECS Fargate + ALB (Blue/Green deployment)
- **Infrastructure as Code** with CloudFormation
- **Automated Rollbacks** with CloudWatch alarms
- **Dependency Management** with AWS CodeArtifact

## 🏗️ Architecture

```
GitHub → CodePipeline → CodeBuild → CodeDeploy → Lambda/ECS
                            ↓
                       CodeArtifact
                            ↓
                       CloudWatch (Monitoring & Rollback)
```

## 📋 API Endpoints

| Endpoint       | Method | Description              |
| -------------- | ------ | ------------------------ |
| `/`            | GET    | Health check             |
| `/health`      | GET    | Detailed health status   |
| `/enroll`      | POST   | Enroll student in course |
| `/enrollments` | GET    | List all enrollments     |
| `/docs`        | GET    | Swagger UI documentation |

## 🧪 Local Development

### Prerequisites

- Python 3.11+
- pip

### Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/student-enrollment-api.git
cd student-enrollment-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest -v

# Start development server
uvicorn app.main:app --reload
```

### Test the API

```bash
# Health check
curl http://localhost:8000/health

# Enroll a student
curl -X POST http://localhost:8000/enroll \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": "STU001",
    "course_id": "AWS101",
    "student_name": "John Doe"
  }'

# View Swagger docs
open http://localhost:8000/docs
```

## 🔧 Tech Stack

**Backend:**

- FastAPI (Python web framework)
- Pydantic (Data validation)
- Pytest (Testing)
- Uvicorn (ASGI server)

**AWS Services:**

- CodePipeline (Orchestration)
- CodeBuild (Build & Test)
- CodeDeploy (Deployment)
- CodeArtifact (Package management)
- Lambda + API Gateway (Serverless deployment)
- ECS Fargate + ALB (Container deployment)
- CloudWatch (Monitoring & Alarms)
- ECR (Container registry)
- CloudFormation (Infrastructure as Code)

**DevOps:**

- Docker (Containerization)
- Git (Version control)
- CloudFormation (IaC)

## 📊 CI/CD Pipeline Features

### Automated Testing

- Unit tests run on every commit
- Integration tests in staging environment
- Build fails if tests don't pass

### Deployment Strategies

**Lambda (Canary):**

- 10% of traffic → new version
- Monitor for 5 minutes
- Automatic rollback if errors detected
- Gradual shift to 100%

**ECS (Blue/Green):**

- Deploy to new task set
- Test with ALB target group
- Shift traffic when healthy
- Keep old version for instant rollback

### Monitoring & Rollback

- CloudWatch alarms on error rates
- Automatic rollback if error rate > 5%
- SNS notifications to team
- Complete audit trail

## 📈 Key Metrics

- **Test Coverage:** 100%
- **Deployment Time:** ~5 minutes
- **Zero-Downtime Deployments:** ✅
- **Automatic Rollbacks:** ✅

## 🎓 Learning Outcomes

This project demonstrates understanding of:

- ✅ CI/CD pipeline automation
- ✅ Infrastructure as Code
- ✅ Containerization & orchestration
- ✅ Multiple deployment strategies
- ✅ Monitoring & observability
- ✅ Automated testing
- ✅ Cloud architecture design

## 📝 License

MIT

## 👤 Author

**Your Name**

- GitHub: [@YourUsername](https://github.com/YourUsername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Portfolio: [yourwebsite.com](https://yourwebsite.com)

---

⭐ Star this repo if you found it helpful!
