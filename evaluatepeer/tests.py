from django.urls import resolve
from django.test import TestCase
from evaluatepeer.views import evaluate


# Create your tests here.
class EvaluatePageTest(TestCase):

    def test_root_url_resolves_to_evaluate_view(self):
        found = resolve('/')
        self.assertEqual(found.func, evaluate)