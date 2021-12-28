from django.urls import path


from .views import UserView, RegistrationAPIView, LoginAPIView

app_name = "service"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('user/', UserView.as_view()),
    path('reg/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),

]