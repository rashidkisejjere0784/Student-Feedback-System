from django.urls import path
from . import views

# URLConf

urlpatterns = [
    path("", views.instructor, name="instructor"),
    path("add_feedback", views.add_feedback, name="add_instructor_feedback"),
    path("view_feedback/<feedback_type>", views.view_feedback,
         name="view_instruction_feedback"),
]
