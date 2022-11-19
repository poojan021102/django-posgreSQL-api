from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Student(models.Model):
    class Meta:
        unique_together = (('student_id','name'),)
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)