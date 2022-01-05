from django.urls import path
from .views import UserRetrieveUpdateAPIView, RegistrationAPIView,LoginAPIView

app_name = "service"

urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view())
]
