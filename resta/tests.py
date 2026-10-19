from django.test import TestCase


class RestaViewTests(TestCase):
    def test_restar_view_returns_difference(self):
        response = self.client.get("/restar/10/3/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "10 - 3 = 7.0")
