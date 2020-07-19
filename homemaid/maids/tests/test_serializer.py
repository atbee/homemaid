from datetime import date

from django.test import TestCase

from ..models import Maid
from ..serializer import MaidSerializer

class TestMaidSerializer(TestCase):
    def test_serializer_should_serialize_object_to_json(self):
        Maid.objects.create(
            name='BB',
            birthdate=date(1998, 4, 29),
            description='Super Maid of the Year',
            certificate='Best Maid 2012',
            salary=3000
        )
        Maid.objects.create(
            name='CC',
            birthdate=date(1998, 9, 30),
            description='Ultra Maid of the Year',
            certificate='Best Maid 2020',
            salary=3200
        )

        maids = Maid.objects.all()
        serializer = MaidSerializer(maids, many=True)

        assert serializer.data == [{'id': 1, 'name': 'BB'}, {'id': 2, 'name': 'CC'}]
