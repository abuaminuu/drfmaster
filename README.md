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
