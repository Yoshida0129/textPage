from django import forms


class TextForm(forms.Form):
    abc = forms.CharField(label="CharField")
    deh = forms.IntegerField(label="IntegerField")
    fields = (abc, deh)

