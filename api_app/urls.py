from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectListAPIView.as_view()),
    path('projects/<slug:slug>/', views.ProjectDetailAPIView.as_view()),
    path('projects/create/', views.ProjectCreateAPIView.as_view()),
    path('contact/', views.ContactCreateAPIView.as_view()),
]
