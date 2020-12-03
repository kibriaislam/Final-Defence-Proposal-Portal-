from django import forms
from django.forms import ModelForm
from myapp.models import defenceInfo


class defenceInfoForm(ModelForm):

    class Meta:
        model = defenceInfo

        fields=['id','sId','sName','batch','semester','email','pNumber','title','description']
