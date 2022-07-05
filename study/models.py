from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

UserModel = get_user_model()


class Teams(models.Model):
    """Кафедра"""
    name = models.CharField(max_length=100, verbose_name='название кафедры')
    image = models.ImageField(verbose_name='изображение кафедры', blank=True, upload_to='image/teams')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'кафедра'
        verbose_name_plural = 'кафедры'


class Teacher(models.Model):
    """Преподаватель"""
    first_name = models.CharField(max_length=50, verbose_name='имя преподавателя')
    middle_name = models.CharField(max_length=50, verbose_name='отчество')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    image = models.ImageField(verbose_name='фотография преподавателя', blank=True, upload_to='image/teacher')
    teams_teacher = models.ForeignKey(Teams, verbose_name='кафедра', on_delete=models.CASCADE)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name='пользователь', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'


class Student(models.Model):
    """Студент"""
    first_name = models.CharField(max_length=50, verbose_name='имя студента')
    middle_name = models.CharField(max_length=50, verbose_name='отчество студента')
    last_name = models.CharField(max_length=50, verbose_name='фамилия студента')
    image = models.ImageField(verbose_name='фотография студента', blank=True, upload_to='image/student')
    teams_student = models.ForeignKey(Teams, verbose_name='кафедра', on_delete=models.CASCADE)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name='пользователь', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'


class HomeWork(models.Model):
    """задание для студента"""
    name = models.CharField(max_length=50, verbose_name='предмет')
    text = models.TextField('поле для домашней работы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'задание'
        verbose_name_plural = 'задания'
