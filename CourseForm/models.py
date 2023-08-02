from django.db import models

# Create your models here.
class Evaluation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    course_code = models.CharField(max_length=50)
    excellent_rating = models.IntegerField()
    very_good_rating = models.IntegerField()
    good_rating = models.IntegerField()
    fair_rating = models.IntegerField()
    poor_rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.course_code}"

#for the technology input under facilty
class Assessment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    course_code = models.CharField(max_length=50)
    excellent_rating = models.IntegerField()
    very_good_rating = models.IntegerField()
    good_rating = models.IntegerField()
    fair_rating = models.IntegerField()
    poor_rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.course_code}"
    
#for class size under facilty
class Coverage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    course_code = models.CharField(max_length=50)
    excellent_rating = models.IntegerField()
    very_good_rating = models.IntegerField()
    good_rating = models.IntegerField()
    fair_rating = models.IntegerField()
    poor_rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.course_code}"

#for class size under facilty
class Impact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    course_code = models.CharField(max_length=50)
    excellent_rating = models.IntegerField()
    very_good_rating = models.IntegerField()
    good_rating = models.IntegerField()
    fair_rating = models.IntegerField()
    poor_rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.course_code}"

#for class size under facilty
class Participation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    course_code = models.CharField(max_length=50)
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
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)
    student_number = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50)
    likes_field = models.CharField(max_length=5000)
    likes_sentiment = models.IntegerField(default=0)
    suggestion_field = models.CharField(max_length=5000)
    suggestion_sentiment = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.course_code}"