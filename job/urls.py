from . import views
from django.urls import path


app_name = 'job'
urlpatterns = [

    path('',views.job_list,name = 'Job_list'),
    path('add',views.add_job,name = 'add_job'),
    path('<str:slug>',views.job_detail,name = 'Job_detail'), #use id in views.
]