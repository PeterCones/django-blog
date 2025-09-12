from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
        
    def test_form_is_invalid_name(self):
        form = CollaborateForm({
            'name':'',
            'email': 'test@test.com',
            'message':'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="name field can be null")
        
    def test_form_is_invalid_email(self):
        form = CollaborateForm({
            'name':'Jon Doe',
            'email': '',
            'message':'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="email field can be null")
        
    def test_form_is_invalid_message(self):
        form = CollaborateForm({
            'name':'Jon Doe',
            'email': 'test@test.com',
            'message':''
        })
        self.assertFalse(form.is_valid(), msg="message field can be null")