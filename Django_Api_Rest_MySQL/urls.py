"""Django_Api_Rest_MySQL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Django API Rest MySQL",
        default_version='1.0.0',
        description="documentation of Pets API",
    ),
    public=True,
)

urlpatterns = [
    # path('docs/', TemplateView.as_view(template_name='docs.html',extra_context={'schema_url':'api_schema'}), name='swagger-ui'),
    # path('', TemplateView.as_view(template_name='docs.html',extra_context={'schema_url':'api_schema'}), name='swagger-ui'),
    # path('api_schema/', get_schema_view(title='Pets API',description='Guide for the REST API'), name='api_schema'),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    re_path(r'^', include("apps.API.urls")),
]


