from django.urls import path
from .views import UserRegistrationAPIView, LoginUserView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
]
