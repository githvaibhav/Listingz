from .views import RetrieveView, RegisterView
from django.urls import path


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('getuser', RetrieveView.as_view())
]

