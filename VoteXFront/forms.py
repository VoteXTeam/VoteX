# form reference from labs1-4

# from django import forms
# from django.forms import ModelForm
#
# from uklonapp.models import Ride
#
# FORMAT_CHOICES = {
#     ('xls', 'xls'),
#     ('csv', 'csv'),
#     ('json', 'json'),
# }
#
#
# class FormatForm(forms.Form):
#     format = forms.ChoiceField(choices=FORMAT_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
#
#
# class RideForm(ModelForm):
#     class Meta:
#         model = Ride
#         fields = '__all__'
