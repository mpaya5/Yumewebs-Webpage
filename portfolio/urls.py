from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.portfolio, name="works"),
    path('<int:work_id>/', views.work, name="work")
]