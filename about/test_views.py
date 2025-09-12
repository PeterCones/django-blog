from django.test import TestCase
from django.urls import reverse
from .views import CollaborateForm
from .models import About

class TestAboutViews(TestCase):
    
    def setUp(self):
        
        self.about = About(title='test', content='test')
        
        self.about.save()
        
    def test_render_about_with_collaborate_form(self):
        
        response = self.client.get(reverse(
            'about'))
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test", response.content)
        self.assertIn(b"test", response.content)

        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
    
    def test_form_submission(self):
        self.client.login(username="myUsername", password="myPassword")
        post_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test collaboration message'
            }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)