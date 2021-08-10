from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Job,Category
from django.core.paginator import Paginator     #make soilder page 1,2,3,4
from .form import ApllyForm,JobForm
from django.utils import timezone
from .filters import JobFilter

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    ## filters
    myfilter = JobFilter(request.GET,queryset = job_list)

    job_list = myfilter.qs

    now = timezone.now()
    paginator = Paginator(job_list, 2) #how many jobs in row.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # category = Category.objects.all()
    context = {'jobs':page_obj , 'time':now ,'myfilter':myfilter}
    return render(request,'job/job_list.html',context)





def job_detail(request,slug):
    job_detail = Job.objects.get(slug = slug) #to return one functions.
    if request.method == 'POST':
        form = ApllyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail # job for forigkey relations.
            myform.save()
    else:
        form = ApllyForm()

    context = {'job':job_detail ,'form':form}
    return render(request,'job/job_detail.html',context)

@login_required   #it's used to make should login befor add jobs.
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user # job for forigkey relations.
            myform.save()
            return redirect(reverse('jobs:Job_list')) #the reverse take name of urls ,
    else:
        form = JobForm()


    return render(request,'job/add_job.html',{'form':form})
