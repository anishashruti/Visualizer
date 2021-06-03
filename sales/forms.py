from django import forms

CHOICES=(
    ('#1','BAR CHART'),
    ('#2','PIE CHART'),
    ('#3','LINE CHART'),
)
RESULT=(
    ('#1','Transaction'),
    ('#2','Sales date'),
)
class SalesSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    chart_type = forms.ChoiceField(choices=CHOICES)
    results_by=forms.ChoiceField(choices=RESULT)