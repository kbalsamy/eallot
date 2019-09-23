from django import forms
from django.forms import ModelForm
from portal.models import Service, Service_Grouping, EDC

# servicegroup form


class SGForm(ModelForm):

    class Meta:
        model = Service
        fields = ['name', 'remarks']


class AddServicesForm(ModelForm):

    serviceZone = forms.ModelChoiceField(label='', queryset=EDC.objects.all(), empty_label="select zone")
    serviceGroup = forms.ModelChoiceField(label='', queryset=Service.objects.all(), empty_label="select Group")

    class Meta:
        model = Service_Grouping
        fields = ['serviceNumber', 'servicePassword', 'serviceZone', 'serviceGroup']
        labels = {'serviceZone': None}
