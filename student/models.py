from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    rool_no = models.IntegerField(unique=True)
    student_class = models.CharField(max_length=50)
    date_of_of_birth = models.DateField(null=True, blank=True)
    adress = models.TextField()
    
    def __str__(self):
        return f"{self.name}({self.rool_no})" 