from django.contrib import admin
from django.urls import path, include
from student import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('students/', include('student.urls')),
    path('teachers/',include('teacher.urls')),
    path('attendance/',include('attendance.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
