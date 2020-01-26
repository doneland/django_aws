from django.urls import path
from myapp.views import index

urlpatterns = [
    path("", index, name="myapp_index"),
]