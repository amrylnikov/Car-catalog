from django.test import TestCase, Client
from django.urls import reverse
from .models import Mark, Model
from unittest.mock import patch

class CarAppTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        mark = Mark.objects.create(name='Toyota')
        Model.objects.create(mark=mark, name='Camry')

        # GET
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Toyota')

        # POST
        response = self.client.post(reverse('index'), {'mark': mark.pk})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Toyota')
        self.assertContains(response, 'Camry')

    @patch('car_app.views.update_autoru_catalog') # Mock
    def test_update_view(self, mock_update_autoru_catalog):
        response = self.client.post(reverse('update'))
        self.assertEqual(response.status_code, 200)
        mock_update_autoru_catalog.assert_called_once()
