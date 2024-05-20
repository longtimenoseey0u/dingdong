from django.urls import path
from clubs.views import lists

urlpatterns = [
    path("lists/", lists),
]