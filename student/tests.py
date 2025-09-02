from django.test import TestCase , Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Student
# Create your tests here.
class HomeViewTests(TestCase):
    # setUp() ek method ha jo test run hony sy pehly automatically chaly ga 
    def setUp(self):
        # Client ek object ha jo ek browesr jesa behave krta ha 
        self.client = Client()
        #  reverse("home") sy ham ny home page ka url fetch keya 
        self.url = reverse("home")
        # yeha user create keya
        self.user = User.objects.create_user(username = "testuser", password="12345")
    
    # yehan cheek lgaya agr user login nhi ha to home page py na jy
    def test_redirect_if_not_logged_in(self):
        # aclient yani browser sy home page py request beji ha 
        response = self.client.get(self.url)
        # agr user login nhi to login page py bejo
        self.assertRedirects(response, '/login/?next=' + self.url)
    
    # test keya user login hony k bad home page py gya ha k nhi
    def test_logged_in_user_can_accsess_home(self):
        # login keya 
        self.client.login(username="testuser",password="12345")
        # browser py url ko fetch keya 
        response = self.client.get(self.url)
        # cheek keya k status code 200 ahya ha k nhi
        self.assertEqual(response.status_code,200)
        # cheek keya k django ny jo templet render kya wo home.html hi tha 
        self.assertTemplateUsed(response,'home.html')
        
class StudentTestCase(TestCase):
    def setUp(self):
        # Fake browser bnana
        self.client = Client()
        # add_student ka urlr fetch krna 
        self.url = reverse('add_student')  
        # user login 
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
    
    def test_add_student(self):
        # model k hisab sy data bnana
        data ={
            'name': 'Ali',
            'rool_no': 20,
            'student_class': '1st',
            'date_of_of_birth': '2000-4-4',
            'adress': 'lhr'
        }
        # data or url ko browser py bejna 
        response = self.client.post(self.url,data)
        # ab cheek krna k page redirect hoa k nhi
        self.assertEqual(response.status_code,302)
        # ab cheek krna k student create hoa k nhi
        self.assertEqual(Student.objects.count(), 1)
        # ab pehla student fetch krna 
        student = Student.objects.first()
        # ab student ka name cheek krna k data wala hi ha k nhi 
        self.assertEqual(student.name, 'Ali')
        # or rool_number cheek
        self.assertEqual(student.rool_no, 20)
    
    def test_add_student_get(self):
        # browser py url beja 
        response = self.client.get(self.url)
        # cheek keya k page load hoa k nhi
        self.assertEqual(response.status_code, 200)
        # ab cheek keya k sai templet load ha k nhi
        self.assertTemplateUsed(response,'student/add_student.html')   
        
class EditStudentTestCase(TestCase): 
    def setUp(self):
        self.client = Client()
        student = Student.objects.create(name='ali', rool_no=1, student_class='1st', adress='lhr', date_of_of_birth='2000-1-1')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.url = reverse('edit_student',args=[student.id])
        
    def test_edit_student(self):
        data = {
            'name':'ahmed',
            'rool_no':3,
            'student_class':'1st',
            'adress':'lhr',
            'date_of_of_birth':'2000-1-1'
        }    
        response = self.client.post(self.url,data)
        self.assertEqual(response.status_code,302)
        student = Student.objects.first()
        self.assertEqual(student.name,'ahmed')
        self.assertEqual(student.rool_no,3)
        
    def test_edit_student_get(self):
        response= self.client.get(self.url)   
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/edit_student.html')
        
class DeleteStudentTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',password='12345')
        self.client.login(username='testuser',password='12345')        
        self.student = Student.objects.create(name='ali',rool_no=12,student_class='2nd',adress='lhr1',date_of_of_birth='2003-4-5')
        self.url = reverse('delete_student', args=[self.student.id])
    def test_delete_student(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code,302)
        self.assertFalse(Student.objects.filter(id=self.student.id).exists())
        
        