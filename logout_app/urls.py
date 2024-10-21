from django.urls import path
from . import views

urlpatterns = [
    path('', views.logout_view, name='logout'),  # Logs the user out after confirmation
]
