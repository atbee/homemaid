import os
from datetime import date
from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase

from ..models import Maid

class TestMaid(TestCase):
    def test_model_should_have_defined_fields(self):
        # Given
        Maid.objects.create(
            name='Atb',
            birthdate=date(1998, 4, 29),
            description='Super Maid of the Year',
            certificate='Best Maid 2020',
            salary=3000
        )

        # When
        maid = Maid.objects.last()
        
        # Then
        self.assertEqual(maid.name, 'Atb')
        self.assertEqual(maid.birthdate, date(1998, 4, 29))
        self.assertEqual(maid.description, 'Super Maid of the Year')
        self.assertEqual(maid.certificate, 'Best Maid 2020')
        self.assertEqual(maid.salary, 3000)

    def test_model_should_have_image_fields(self):
        # Given
        mock = MagicMock(spec=File)
        mock.name = 'profile.png'

        Maid.objects.create(
            name='Atb',
            profile_image=mock,
            birthdate=date(1998, 4, 29),
            description='Super Maid of the Year',
            certificate='Best Maid 2020',
            salary=3000
        )

        # When
        maid = Maid.objects.last()
        
        # Then
        self.assertEqual(maid.profile_image.name, 'profile.png')

        os.remove('profile.png')