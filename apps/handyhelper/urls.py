from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboardView),
    url(r'^user/(?P<id>\d+)/$', views.userJobsView),
    url(r'^add/(?P<id>\d+)/$', views.addJobEvent),
    url(r'^addJob/$', views.addNewJobView),
    url(r'^addJob/add/$', views.addNewJobForm),
    url(r'^editJob/(?P<id>\d+)/$', views.editJobPlanView),
    url(r'^editJob/edit/(?P<id>\d+)/$', views.editJobPlanrForm),
    url(r'^cancel/(?P<id>\d+)/$', views.cancelJobEvent),
    url(r'^delete/(?P<id>\d+)/$', views.deleteJobEvent),
    url(r'^viewJobplans/(?P<id>\d+)/$', views.viewJobPlans),
]
