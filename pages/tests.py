from django.test import SimpleTestCase  #used for tests that don't involve database
from django.urls import reverse

# Create your tests here.

class HomepageTests(SimpleTestCase): 
    def test_url_exists_at_correct_location(self):  #test the URL location
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):   #tests the URL name
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):   #tests that the correct template is used on the page
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):    #tests that the expected content is displayed
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")

class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): 
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): 
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")

