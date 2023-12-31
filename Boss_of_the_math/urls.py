"""
URL configuration for Boss_of_the_math project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from calculator import views

urlpatterns = [
    path('', views.index, name='index'),
    path("calculator/", views.calc, name='calc'),
    path("mat_calc/", views.matrix_calc, name='matrix_calc'),
    path('calculator/result/', views.result, name='result'),
    path('bin_calc/', views.binary_calc, name='binary_calc'),
    path('bin_calc/result/', views.binary_result, name='binary_result'),
    path('mat_problems/', views.MathematicalProblemListView.as_view(), name='mat_problems'),
    path('admin/', admin.site.urls),
]
