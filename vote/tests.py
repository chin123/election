from django.test import TestCase
from . import views

# Create your tests here.
class TestZero(TestCase):
    def test_lock_is_zero(self):
        """ Lock should be 0 at the start of the program """
        self.assertEqual(views.lock,0)
    def test_count_is_zero(self):
        """ Vote count should be 0 at the start of the program """
        for i in views.names:
            for j in views.names[i]:
                self.assertEqual(j["count"],0)
