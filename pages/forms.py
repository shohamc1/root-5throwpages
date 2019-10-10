from django import forms 
from .models import pagecontent
  
class FifthForm(forms.ModelForm): 
  
    class Meta: 
        model = pagecontent 
        fields = ['id', 'name', 'shortdesc', 'desc1', 'desc2', 'photo'] 