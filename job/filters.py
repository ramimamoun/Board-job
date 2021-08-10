#pip install django-filter
import django_filters
from .models import Job
from django_filters import DateFilter,CharFilter

class JobFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='published_time',lookup_expr='gte')
    end_date = DateFilter(field_name='published_time',lookup_expr='lte')
    title = CharFilter(field_name='title',lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['title','image','published_time','slug','salary','Vacancy','owner']
