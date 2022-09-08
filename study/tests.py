from django.test import TestCase

from .models import HomeWork


class TestHomeWork(TestCase):

    @classmethod
    def setUpTestData(cls):
        HomeWork.objects.create(name='mat', text='это математика')

    def test_name(self):
        author = HomeWork.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')



class TestStudentList(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass