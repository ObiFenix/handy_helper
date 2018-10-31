from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homeView),
    url(r'^register/$', views.registerView),
    url(r'^logout/$', views.logoutView),
    url(r'^login/$', views.loginView,name='login'),
    url(r'^login/user/$', views.loginUserForm),
    url(r'^register/user/$', views.registerUserForm),
]
