from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student

# Show home page
@login_required
def home(request):
    return render(request, 'home.html') 

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

# Show student list page
@api_view(['GET','POST'])
def student_list_api(request):
    if request.method == 'GET':
       students = Student.objects.all()
       serializer = StudentSerializer(students, many=True)
       return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def add_student_api(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)      
  
# Show add student form and save data
@login_required
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        rool_no = request.POST.get('rool_no')
        student_class = request.POST['student_class']
        adress = request.POST['adress']
        dob = request.POST['date_of_of_birth']
        Student.objects.create(name=name, rool_no=rool_no, student_class=student_class, adress=adress,  date_of_of_birth=dob)
        return redirect('student_list')
    return render(request, 'student/add_student.html')

@api_view(['GET','PUT','DELETE'])
def edit_student_api(request,id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'PUT':
       serializer = StudentSerializer(instance=student, data=request.data)
       if serializer.is_valid(raise_exception=True):
           serializer.save()
           return Response(serializer.data)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
         serializer = StudentSerializer(instance=student)
         return Response(serializer.data)

@login_required
def edit_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.rool_no = request.POST['rool_no']
        student.student_class = request.POST['student_class']
        student.adress = request.POST['adress']
        student.date_of_of_birth = request.POST['date_of_of_birth']
        student.save()
        return redirect ('student_list')
    return render(request, 'student/edit_student.html',{'student': student})

@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')    