from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'user/login_user.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

    def logout_view(request):
        logout(request)
        return redirect('home')