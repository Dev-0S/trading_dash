from django.urls import path
from .views import position_dashboard

urlpatterns = [
    path('', position_dashboard, name='position_dashboard'),
]
