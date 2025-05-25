from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('upload/', views.upload_resume, name='upload_resume'),
    path('<int:pk>/', views.resume_detail, name='resume_detail'),
    path('<int:pk>/delete/', views.delete_resume, name='delete_resume'),
    path('review/', views.review_resume, name='review_resume'),
] 