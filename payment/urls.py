from django.urls import path
from .views import VerifyView

app_name = "payment"
urlpatterns = [
    path('verify/', VerifyView, name='Verify')
]
