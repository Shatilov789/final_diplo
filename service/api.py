from django.urls import path
from .views import UserRetrieveUpdateAPIView, RegistrationAPIView, LoginAPIView,  InfoListProduct, PartnerUpdate

app_name = "service"

urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('update/', PartnerUpdate.as_view()),
    path('info/', InfoListProduct.as_view())
]
