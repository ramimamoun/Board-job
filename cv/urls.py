from . import views
from .views import CustomerListView ,create_cv,GaneratePDF
from django.urls import path


app_name = 'cv'
urlpatterns = [

    path('create_cv',create_cv,name = 'create_cv'),
    # path('pdf',views.pdf,name = 'pdf'),
    path('xp',CustomerListView.as_view(),name = 'customer_listview'),
    path('pdf',GaneratePDF.as_view(),name = 'pdf'),
]