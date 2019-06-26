from django import forms
from.models import Bitly

class BitlyForm(forms.ModelForm):
    class Meta:
        model=Bitly
        fields= ['long_url']

class editBitly(forms.ModelForm):
    class Meta:
        model=Bitly
        fields=["long_url","Shortcode"]        