from django import forms
from .models import Profile

class userProfile(forms.ModelForm):
    phone = forms.CharField(label="Phone Number:", widget=forms.TextInput(attrs={'class':'form control','placeholder':'Phone Number'}),required=False)
    address1 = forms.CharField(label="Address1:", widget=forms.TextInput(attrs={'class':'form control','placeholder':'address'}),required=False)
    address2 = forms.CharField(label="Address2:", widget=forms.TextInput(attrs={'class':'form control','placeholder':'address2'}),required=False)
    city = forms.CharField(label="City:", widget=forms.TextInput(attrs={'class':'form control','placeholder':'city'}),required=False)
    state = forms.CharField(label="State:", widget=forms.TextInput(attrs={'class':'form control','placeholder':'state'}),required=False)
    zipcode = forms.CharField(label="Zipcode:", widget=forms.TextInput(attrs={'class':'form control','placeholder':'zipcode'}),required=False)
    country = forms.CharField(label="Country:", widget=forms.TextInput(attrs={'class':'form control','placeholder':'country'}),required=False)
    
    class Meta:
        model = Profile
        fields = ('phone','address1','address2','city','state','zipcode','country',)