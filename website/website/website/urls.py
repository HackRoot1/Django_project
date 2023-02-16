"""website URL Configuration

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
from django.urls import path
from website import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('units/', views.units, name = "units"),
    path('reference_books/', views.reference_books, name = "reference_books"),
    path('subject1/<sem>', views.subject1, name = "subject1"),
    path('subject2/', views.subject2, name = "subject2"),
    path('subject3/', views.subject3, name = "subject3"),
    path('login/', views.login, name = "login"),
]
