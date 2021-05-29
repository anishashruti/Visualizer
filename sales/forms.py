from django import forms

CHOICES=(
    ('#1','BAR'),
    ('#2','PIE'),
    ('#1','LINE'),
)

class SalesSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    chart_type = forms.ChoiceField(choices=CHOICES)