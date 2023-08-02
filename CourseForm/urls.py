from django.urls import path
from . import views

#URLConf

urlpatterns = [
    path("", views.course, name="course"),
    path("add_feedback", views.add_feedback, name="add_course_feedback")
]