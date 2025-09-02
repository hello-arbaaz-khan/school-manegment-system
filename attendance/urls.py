from django.urls import path
from . import views

urlpatterns = [
    path('mark/', views.mark_attendance, name='mark_attendance'),  # ✅ form page
    path('list/', views.attendance_list, name='attendance_list'),  # ✅ display page
    path('edit/<int:id>/', views.edit_attendance, name='edit_attendance'),
    path('delete/<int:id>/', views.delete_attendance, name='delete_attendance'),
]
