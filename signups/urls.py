from django.urls import path
from signups.views import signup

urlpatterns = [
    path("signup/", signup),
]