from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15, unique=True)
    join_date = models.DateField()
    
    def __str__(self):
        return self.name

class TeacherAttendance(models.Model):
        teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
        date = models.DateField()
        status = models.CharField(max_length=10,choices=[('Present','Present'),('Absent','Absent')])
    