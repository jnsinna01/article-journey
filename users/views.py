from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreation, CustomUserChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm


class SignUpView(CreateView):
    form_class = CustomUserCreation
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProfileEditView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'edit_profile.html'

    def get_object(self):
        return self.request.user


class PassWordEditView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('home')