from django.urls import path

from . import views

urlpatterns = [
    path("kvadrat", views.kvadratTenliyi.as_view(), name="kvadratTenliyi"),
]
