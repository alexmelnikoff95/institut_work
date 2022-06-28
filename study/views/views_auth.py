from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout


# class LoginUser(LoginView):
#     """Авторизация на сайте"""
#     form_class = UserLoginForm
#     template_name = 'login.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return dict(list(context.items()))
#
#     def get_success_url(self) -> str:
#         return reverse_lazy('index')


# class RegisterUser(CreateView):
#     """Регистрация пользователей"""
#     form_class = UserRegisterForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return dict(list(context.items()))
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('home')

#
# def user_logout(request):
#     """Выход из профиля"""
#     logout(request)
#     return redirect('login')
