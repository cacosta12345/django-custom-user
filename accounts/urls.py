from django.urls import path

from .views import SignUpView, index

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", index, name="index")
]