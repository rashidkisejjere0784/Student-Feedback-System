from django.db import models

# Create your models here.
class ClassroomFacilty(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    facilty_name = models.CharField(max_length=50)
    excellent_rating = models.IntegerField()
    very_good_rating = models.IntegerField()
    good_rating = models.IntegerField()
    fair_rating = models.IntegerField()
    poor_rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.facilty_name}"

#for the technology input under facilty
class TechnologyFacilty(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    facilty_name = models.CharField(max_length=50)
    excellent_rating = models.IntegerField()
    very_good_rating = models.IntegerField()
    good_rating = models.IntegerField()
    fair_rating = models.IntegerField()
    poor_rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.facilty_name}"
    
#for class size under facilty
class ClassSizeFacilty(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    facilty_name = models.CharField(max_length=50)
    excellent_rating = models.IntegerField()
    very_good_rating = models.IntegerField()
    good_rating = models.IntegerField()
    fair_rating = models.IntegerField()
    poor_rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.facilty_name}"