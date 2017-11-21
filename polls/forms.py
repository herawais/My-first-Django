from django import forms
class add_student_form(forms.Form):
    name = forms.CharField()
    fname = forms.CharField()
    rollNo = forms.CharField()