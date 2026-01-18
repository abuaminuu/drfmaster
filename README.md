# Django REST Framework Snippets API

## Overview
A complete REST API implementation following the official Django REST Framework tutorial. This application provides CRUD operations for code snippets with user authentication, permissions, and automated API documentation via Swagger/OpenAPI.

## Features
- **Full CRUD Operations**: Create, read, update, and delete code snippets
- **User Authentication**: Session-based and token authentication
- **Permissions System**: Fine-grained control over API access
- **Hyperlinked APIs**: RESTful HATEOAS-compliant responses
- **Interactive Documentation**: Auto-generated Swagger/OpenAPI docs
- **Multiple Formats**: JSON and browsable HTML API support

## Quick Start

### Installation
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### API Endpoints
- `/` - API root with hyperlinks to all resources
- `/snippets/` - List and create code snippets
- `/snippets/{id}/` - Retrieve, update, or delete specific snippets
- `/users/` - List and view user profiles
- `/api-auth/` - Session authentication endpoints
- `/swagger/swagger/` - Interactive API documentation

## Documentation
Access the complete interactive API documentation at `/swagger/` after starting the server. The Swagger interface provides:
- Live API endpoint testing
- Request/response schemas
- Authentication demonstration
- Code sample generation

## Authentication
- **Session Auth**: Use `/api-auth/login/` for browser-based access
- **Permissions**: 
  - Anonymous users: Read-only access
  - Authenticated users: Full CRUD on owned snippets
  - Staff users: Administrative privileges

# Django REST API with Celery & Swagger Documentation

## 🚀 Quick Overview
A production-ready Django REST Framework API with asynchronous task processing and comprehensive API documentation. This application implements the official DRF tutorial code snippets API enhanced with Celery for background tasks and Swagger for interactive API documentation.

## ✨ Key Features
- **RESTful API**: Full CRUD operations for code snippets with user authentication
- **Background Processing**: Celery-powered asynchronous email notifications
- **Interactive Documentation**: Auto-generated Swagger/OpenAPI 3.0 documentation
- **Production Ready**: Configured for deployment on Render with Redis and PostgreSQL
- **HATEOAS Compliance**: Hyperlinked API responses following REST best practices

## 📋 Prerequisites
- Python 3.9+
- PostgreSQL or SQLite
- Redis (for Celery broker)
- Git

## 🛠️ Installation & Setup
```bash
# Clone repository
git clone <repository-url>
cd django-snippets-api

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Database setup
python manage.py migrate
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## 🔧 Services
- **API Server**: `localhost:8000` - Django REST Framework with browsable API
- **Celery Worker**: Background task processing (email notifications)
- **Swagger UI**: `localhost:8000/swagger/` - Interactive API documentation
- **ReDoc**: `localhost:8000/redoc/` - Alternative API documentation

## 🌐 Deployment
The application is pre-configured for seamless deployment on Render:
1. Automatic PostgreSQL provisioning
2. Redis integration for Celery
3. SSL certificates with custom domain support
4. Zero-downtime deployments

## 📚 API Endpoints
- `GET /` - API root with resource links
- `GET /swagger/` - Interactive API documentation
- `POST /api/snippets/` - Create new code snippets
- `POST /api/send-email/` - Trigger async email notifications
- `GET /api/users/` - User management endpoints

## 🔒 Authentication
- Session-based authentication for browser access
- Token authentication for API clients
- Granular permissions: read-only for anonymous users, full CRUD for authenticated users

Perfect for learning Django REST Framework patterns or as a production API template with modern tooling and deployment-ready configuration.
