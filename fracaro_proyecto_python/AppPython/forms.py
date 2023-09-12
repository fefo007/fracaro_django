from django import forms

class OrdersForm(forms.Form):
    client = forms.CharField(max_length=25,required=True)
    travel = forms.CharField(max_length=25,required=True)
    departure = forms.DateField(required=True)
    arrival = forms.DateField(required=True)

class TravelForm(forms.Form):
    name = forms.CharField(max_length=25,empty_value=None,help_text='nombre',required=True)
    image = forms.CharField(max_length=300,empty_value=None,help_text='url',required=True)
    price = forms.IntegerField(help_text='precio',required=True)
    time = forms.CharField(max_length=25,empty_value=None,help_text='dias',required=True)
    description = forms.CharField(max_length=50,empty_value=None,help_text='descripcion',required=True)