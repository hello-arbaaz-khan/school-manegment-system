from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.decorators import login_required
from .models import Teacher
from .models import TeacherAttendance
from datetime import datetime
# Create your views here.
@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html',{'teachers': teachers})

@login_required
def add_teacher(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        join_date = request.POST['join_date']
        Teacher.objects.create(name=name, subject=subject, email=email, phone_no=phone_no, join_date=join_date)
        return redirect('teacher_list')
    return render(request, 'teacher/add_teacher.html')

@login_required
def mark_teacher_attendance(request):
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        for teacher in teachers:
            status = request.POST.get(f"status_{teacher.id}")
            if status:
                TeacherAttendance.objects.create(teacher=teacher,date=datetime.now(),status=status)
        return redirect('teacher_attendance_list')
    return render(request, 'teacher/mark_teacher_attendance.html', {'teachers': teachers})
def teacher_attendance_list(request):
    attendance = TeacherAttendance.objects.select_related('teacher').order_by('-date')
    return render(request, 'teacher/teacher_attendance_list.html', {'attendances': attendance})

@login_required
def edit_teacher(request,id):
    teacher = get_object_or_404(Teacher,id=id)
    if request.method == 'POST':
        teacher.name = request.POST['name']
        teacher.subject = request.POST['subject']
        teacher.email = request.POST['email']
        teacher.phone_no = request.POST['phone_no']
        teacher.join_date = request.POST['join_date']
        teacher.save()
        return redirect ('teacher_list')
    return render(request, 'teacher/edit_teacher.html',{'teacher': teacher})

@login_required
def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return redirect('teacher_list') 

@login_required
def edit_teacher_attendance(request, id):
    attendance = get_object_or_404(TeacherAttendance, pk=id)
    teachers = Teacher.objects.all()  # Fetch all teachers for the dropdown

    if request.method == 'POST':
        teacher_id = request.POST['teacher']
        attendance.teacher = Teacher.objects.get(id=teacher_id)
        attendance.date = request.POST['date']
        attendance.status = request.POST['status']
        attendance.save()
        return redirect('teacher_attendance_list')

    return render(request, 'teacher/edit_teacher_attendance.html', {
        'attendance': attendance,
        'teachers': teachers
    })


@login_required
def delete_teacher_attendance(request,id):
    attendance = get_object_or_404(TeacherAttendance,id=id)
    if request.method == 'POST':
        attendance.delete()
        return redirect('teacher_attendance_list')
    return render(request,'teacher/delete_teacher_attendance.html',{'attendance':attendance})
