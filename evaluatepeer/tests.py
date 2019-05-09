from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from evaluatepeer.views import evaluate


# Create your tests here.
class EvaluatePageTest(TestCase):

    def test_root_url_resolves_to_evaluate_view(self):
        found = resolve('/')
        self.assertEqual(found.func, evaluate)

    def test_index_page_returns_correct_html(self):
        request = HttpRequest()
        response = evaluate(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>PAF</title>', html)
        self.assertTrue(html.endswith('</html>'))