from datetime import date

from django.test import TestCase
from django.urls import reverse

from ..models import Maid


class TestMaidListView(TestCase):
    def test_view_should_respond_200(self):
        response = self.client.get(reverse('maid-list'))
        assert response.status_code == 200

    def test_view_should_display_maid_list(self):
        Maid.objects.create(
            name='Atb',
            birthdate=date(1998, 4, 29),
            description='Super Maid of the Year',
            certificate='Best Maid 2020',
            salary=3000
        )

        Maid.objects.create(
            name='Zkan',
            birthdate=date(1997, 2, 10),
            description='Ultra Maid of the Year',
            certificate='Oh Maid 2020',
            salary=2800
        )

        response = self.client.get(reverse('maid-list'))

        assert '<li>Atb</li>' in str(response.content)
        assert '<li>Zkan</li>' in str(response.content)