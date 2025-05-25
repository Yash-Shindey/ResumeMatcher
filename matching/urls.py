from django.urls import path
from . import views

urlpatterns = [
    path('', views.match_list, name='match_list'),
    path('<int:pk>/', views.match_detail, name='match_detail'),
    path('generate/<int:resume_id>/', views.generate_matches, name='generate_matches'),
] 