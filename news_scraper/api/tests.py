from django.test import TestCase
from .models import News

# Create your tests here.
class ScrapeTestCase(TestCase):
    """This class defines the testing for the Scraping Capability and News model."""
    def test_scrape(self):
        """Insert keyword for test here """
        keyword = ["COVID", "Libur", "Deloitte", "Jakarta Barat", "Banjir Bandang"]
        for i in range(len(keyword)):
            response = self.client.get("/v1/news/", params = {"keyword": keyword[i]})
            self.assertEqual(response.status_code, 200)

