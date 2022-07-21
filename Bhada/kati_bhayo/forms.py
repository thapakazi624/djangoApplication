from django import forms

# creating a form to display in the landing page
class katibhayoForm(forms.Form):
    distance = forms.IntegerField(label="Distance Covered (in KM)")
    time_stamp = forms.TimeField(label="Time of the travel(hh:mm)")


