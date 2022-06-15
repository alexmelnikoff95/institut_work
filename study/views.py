from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Teams, Student, Teacher

from django.views import View


class BaseContextView(View):
    page_title = None
    extra_context = {}
    template = None

    def get_context(self, **kwargs):
        return {
            **self.extra_context,
            **kwargs,
            'page_title': self.page_title
        }

    def render_response(self, context=None):
        if not context:
            context = {}
        assert self.template, 'шаблон должен быть задан'
        return render(self.request, self.template, self.get_context(**context))


class IndexView(BaseContextView):
    page_title = 'выбор кафедры'
    template = 'index.html'

    def get(self, request):
        teams = Teams.objects.all()
        return self.render_response(context={'teams': teams})


class StudentListView(BaseContextView):
    page_title = 'выбор студента'
    template = 'student_list.html'

    def get(self, request):
        st = Student.objects.all()
        return self.render_response(context={'student': st})


class StudentDetailView(BaseContextView):
    page_title = 'домашние задание для студента'
    template = 'home_work.html'

    def get(self, request, id):
        st = get_object_or_404(Student, pk=id)
        return self.render_response(context={'st': st})
