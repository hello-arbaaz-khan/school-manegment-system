from django.shortcuts import get_object_or_404, render,redirect
from .models import Attendance
from student.models import Student
from datetime import datetime
# Create your views here.
def mark_attendance(request):
    students = Student.objects.all() # fetch all students records
    if request.method == 'POST':
        for student in students:
            status = request.POST.get(f"status_{student.id}") # Get attendance statue
            Attendance.objects.create(student=student, date=datetime.now(), status=status) # create attendance record
        return redirect('attendance_list')
    return render(request, 'attendance/mark_attendance.html', {'students': students}) # Pass the templates 
            
def attendance_list(request):
    attendances = Attendance.objects.select_related('student').order_by('-date') # Fetch  attendance with student data
    return render(request, 'attendance/attendance_list.html', {'attendances': attendances}) # Pass the templates 

def edit_attendance(request,id):
    attendance = get_object_or_404(Attendance,id=id)
    if request.method == 'POST':
        attendance.name = request.POST['name']
        attendance.save()
        return redirect ('attendance_list')
    return render(request, 'attendance/edit_attendance.html',{'attendance': attendance})

def delete_attendance(request, id):
    attendance = get_object_or_404(Attendance, id=id)
    attendance.delete()
    return redirect('attendance_list')                    