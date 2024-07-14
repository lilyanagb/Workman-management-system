from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class LogInTest(TestCase):


    def setUp(self):
        self.register_url=reverse('users-registration')
        self.login_url=reverse('users-login')
        self.user={
            'email':'lilzpp17@gmail.com',
            'username':'George',
            'password':'gbelchev66',
            'password2':'gbelchev66',
        }
        self.user_unmatching_password={
            'email':'lilzpp17@gmail.com',
            'username':'Emily',
            'password':'gbelchev66',
            'password2':'lqlq',
        }
        self.user_invalid_name={
            'email':'lilzpp17@gmail.com',
            'username':'Petar',
            'password':'gbelchev66',
            'password2':'gbelchev66',
        }
        return super().setUp()
    
class RegisterTest(LogInTest):


    def test_can_view_page_correctly(self):
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'users/registration.html')

    # def test_can_register_user(self):
    #     response=self.client.post(self.register_url,self.user,format='text/html')
    #     self.assertEqual(response.status_code,302)

    # def test_cant_register_user_with_unmatching_passwords(self):
    #     response=self.client.post(self.register_url,self.user_unmatching_password,format='text/html')
    #     self.assertEqual(response.status_code,400)

    # def test_cant_register_user_with_invalid_email(self):
    #     response=self.client.post(self.register_url,self.user_invalid_name,format='text/html')
    #     self.assertEqual(response.status_code,400)

    # def test_cant_register_user_with_taken_email(self):
    #     self.client.post(self.register_url,self.user,format='text/html')
    #     response=self.client.post(self.register_url,self.user,format='text/html')
    #     self.assertEqual(response.status_code,400)

class LoginTest(LogInTest):


    def test_can_access_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'users/login.html')

    # def test_login_success(self):
    #     self.client.post(self.register_url,self.user,format='text/html')
    #     user=User.objects.filter(email=self.user['email']).first()
    #     user.is_active=True
    #     user.save()
    #     response= self.client.post(self.login_url,self.user,format='text/html')
    #     self.assertEqual(response.status_code,302)

    # def test_cantlogin_with_no_username(self):
    #     response= self.client.post(self.login_url,{'username':'','password':'gbelchev66'},format='text/html')
    #     self.assertEqual(response.status_code,401)

    # def test_cantlogin_with_no_password(self):
    #     response= self.client.post(self.login_url,{'username':'Georgi','password':''},format='text/html')
    #     self.assertEqual(response.status_code,401)