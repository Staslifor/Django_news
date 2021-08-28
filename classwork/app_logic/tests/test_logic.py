from django.test import SimpleTestCase
from classwork.app_logic.helpers import check_access_by_age


class BuisnessLogicTest(SimpleTestCase):
    def test_access_denied(self):
        self.assertFalse(check_access_by_age(17))
