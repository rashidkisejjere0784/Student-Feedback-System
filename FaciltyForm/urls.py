from django.urls import path
from . import views

#URLConf

urlpatterns = [
    path("", views.facility, name="facility"),
    path("add_feedback/", views.add_feedback, name="add_facility_feedback")
]