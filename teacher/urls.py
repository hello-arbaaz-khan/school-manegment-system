from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('add/', views.add_teacher, name='add_teacher'),
    path('edit/<int:id>/', views.edit_teacher, name='edit_teacher'),
    path('delete/<int:id>/', views.delete_teacher, name='delete_teacher'),
    path('mark/',views.mark_teacher_attendance,name='mark_teacher_attendance'),
    path('list/',views.teacher_attendance_list,name='teacher_attendance_list'),
    path('attendance/edit/<int:id>/', views.edit_teacher_attendance, name='edit_teacher_attendance'),
    path('attendance/delete/<int:id>/', views.delete_teacher_attendance, name='delete_teacher_attendance'),
]
