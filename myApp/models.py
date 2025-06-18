from django.db import models
import pickle
# Create your models here.
class Student_Profile(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)
    marks = models.IntegerField()
    photo = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return f"{self.name} - {self.roll_no}"
