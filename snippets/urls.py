"""
URL configuration for drfmaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# Create a router and register our ViewSets with it.
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"snippets", views.SnippetViewSet, basename="snippet")

# the API urls are now determined automatically by the router
urlpatterns = [
    path("", include(router.urls)),
]


