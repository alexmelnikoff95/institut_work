from django.urls import path

from .views import IndexView, StudentListView, StudentDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('student-list', StudentListView.as_view(), name='student_list'),
    path('home-work/<int:id>', StudentDetailView.as_view(), name='home_work')
]
