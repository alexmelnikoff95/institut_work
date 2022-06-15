from django.db import models


class Teams(models.Model):
    """Кафедра"""
    name = models.CharField(max_length=100, verbose_name='название кафедры')

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
    teams_teacher = models.ForeignKey(Teams, verbose_name='кафедра', on_delete=models.CASCADE)

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
    teams_student = models.ForeignKey(Teams, verbose_name='кафедра', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
