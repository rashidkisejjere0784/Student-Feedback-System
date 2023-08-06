from django.urls import path
from . import views

#URLConf

urlpatterns = [
    path("", views.facility, name="facility"),
    path("add_feedback/", views.add_feedback, name="add_facility_feedback"),
    path("view_feedback/<feedback_type>", views.view_feedback, name="view_facility_feedback")
]