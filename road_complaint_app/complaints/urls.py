from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('review_feedback/<int:complaint_id>/', views.review_feedback, name='review_feedback'),
    path('signup/', views.signup, name='signup'),
]

