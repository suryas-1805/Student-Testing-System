from django.db import models

# Create your models here.
class Student_Details(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    contact=models.IntegerField(unique=True)
    password=models.CharField(max_length=10)
    score=models.IntegerField(default=False)
    testing=models.IntegerField(default=False)

    def __str__(self):
        return self.name
    