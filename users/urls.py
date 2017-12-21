from django.conf.urls import url
from .views import UserRegister
urlpatterns = [
    url(r'^sign_up/$', UserRegister.as_view() ,name='user-sign-up'),
]