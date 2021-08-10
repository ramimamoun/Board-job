from django import forms
from .models import Aplly,Job

class ApllyForm(forms.ModelForm):
    class Meta:
        model = Aplly
        fields = ['name','email','weblink','cv','cover_letter']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('owner', 'slug',)


