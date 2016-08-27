from django.conf.urls import url
from apps.users.views import home
from apps.users.views import login_view
from apps.users.views import logout_view
from apps.users.views import RegistrationView


app_name = 'users'
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', RegistrationView.as_view(), name='register'),
]