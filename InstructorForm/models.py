from django.db import models

# Create your models here.
class TeachingRate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    instructor_name = models.CharField(max_length=50)
    excellent_rating = models.IntegerField()
    very_good_rating = models.IntegerField()
    good_rating = models.IntegerField()
    fair_rating = models.IntegerField()
    poor_rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.course_code}"

#for the technology input under facilty
class InteractionRate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    instructor_name = models.CharField(max_length=50)
    excellent_rating = models.IntegerField()
    very_good_rating = models.IntegerField()
    good_rating = models.IntegerField()
    fair_rating = models.IntegerField()
    poor_rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.course_code}"
    

#for the quantitative
class QuatitativeFeedback(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    instructor_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)
    student_number = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50)
    likes_field = models.CharField(max_length=5000)
    likes_sentiment = models.IntegerField(default=0)
    suggestion_field = models.CharField(max_length=5000)
    suggestion_sentiment = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.course_code}"