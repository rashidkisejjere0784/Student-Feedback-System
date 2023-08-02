from django.urls import path
from . import views

#URLConf

urlpatterns = [
    path("", views.instructor, name="instructor"),
    path("add_feedback", views.add_feedback, name="add_instructor_feedback")
]