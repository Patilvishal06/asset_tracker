from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from CustUserAuth.forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs['class'] = 'form-control'
        form.fields['username'].widget.input_type = 'email'
        form.fields['username'].widget.attrs['name'] = 'email'
        form.fields['password'].widget.attrs['class'] = 'form-control'
        form.fields['remember_me'].widget.attrs['id'] = 'remember'
        return form

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
        return super().form_valid(form)




class CustomLogoutView(LogoutView):
    next_page = 'login'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'