from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate 
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from apps.users.forms import CustomUserCreationForm


def home(request):
    return render(request, 'user/home.html')


def login_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:home'))

    kwargs['extra_context'] = {'next': reverse('users:home')}
    kwargs['template_name'] = 'user/login.html'
    return login(request, *args, **kwargs)


def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('users:login')
    return logout(request, *args, **kwargs)


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')    
    template_name = 'user/register.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        is_valid = form.is_valid()
        response = super().post(request, *args, **kwargs)

        if is_valid:
            new_user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            auth_login(request, new_user)
            return HttpResponseRedirect(reverse_lazy('users:home'))
        return response