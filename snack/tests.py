from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack
from django.utils import timezone
# Create your tests here.
class SnackTest(TestCase):
    
    def setUp(self):
        self.user=get_user_model().objects.create_user(username="lion", email="lion@lion.com",password="lion")
        self.snack = Snack.objects.create(name="pizzaaaaa", description="nicepizzzaaa", purchaser=self.user)



    def test_snack_list_status_code(self):

        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    

    def test_snack_list_template(self):
 
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack/snack_list.html")  

    def test_published_post(self):
        self.client.post(path='snack_list/create/',name="pizzaaaaa", description="nicepizzzaaa", purchaser=self.user)
        self.assertEqual(self.snack.name, "pizzaaaaa")

    def test_contents(self):
        
        self.assertEqual(str(self.snack), "pizzaaaaa")

    def test_name(self):
        
        self.assertEqual(str(self.snack), "pizzaaaaa")

    def test_description(self):
        
        self.assertEqual(str(self.snack.description), "nicepizzzaaa")
    
    def test_user(self):
        
        self.assertEqual(str(self.user), "lion@lion.com")
    
    def test_delete(self):
        response = self.client.get(reverse("snack_delete", args="1")).status_code
        self.assertEqual(response, 200)