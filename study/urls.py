from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from study.views.views import IndexView, StudentListView, StudentDetailView
from study.views.views_auth import RegisterUser

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('student-list', StudentListView.as_view(), name='student_list'),
    path('home-work/<int:id>', StudentDetailView.as_view(), name='home_work'),

    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    # path('logout/', user_logout, name='logout'),
]
