from django.urls import path
from . import views

#URLConf

urlpatterns = [
    path("", views.course, name="course"),
    path("add_feedback", views.add_feedback, name="add_course_feedback"),
    path("view_feedback/<feedback_type>", views.view_feedback, name="view_course_feedback")
]