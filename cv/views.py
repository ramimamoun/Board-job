from django.shortcuts import render
from .models import Info
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import Info
from django.views.generic import View
from .utils import render_to_pdf
##pip install xhtml2pdf

# Create your views here.

## the first way :
def create_cv(request,*args,**kwargs):
    template_path = 'cv/xp.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download :
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if displayed :
    response['Content-Disposition'] = 'filename="report.pdf"'

# find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')


    return response

def pdf(request,*args,**kwargs):
    pass

    return render(request,'cv/xp.html',{})

class CustomerListView(ListView):
    model = Info
    template_name = 'cv/xp.html'
## the sucound way :
class GaneratePDF(View):
    def get(self,request,*args,**kwargs):
        template = get_template('cv/xp.html')
        # context = {}
        html = template.render({})
        pdf = render_to_pdf('cv/xp.html',{})
        if pdf:
            response = HttpResponse(pdf,content_type='application/pdf')
            # filename = "pdf_%s.pdf" %("123432")
            # content = "inline; filename='%s'"%(filename)
            # download = request.GET.get("download")
            # if download:
                # content = "attachment; filename='%s'"%(filename)
            # response['Content-Disposition']=content
            return response
        return HttpResponse("Not found ...!")
    # def generate_view(self,request,*args,**kwargs):
    #     template = get_template('cv/pdf.html')
    #     # context = {}
    #     html = template.render({})
    #     return HttpResponse(html)



