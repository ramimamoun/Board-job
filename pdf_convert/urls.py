from django.urls import path

from . import views
app_name = 'pdf_convert'

urlpatterns = [
    path('showproducts', views.show_products, name='showproducts'),
    path('create-pdf', views.pdf_report_create, name='create-pdf'),
]