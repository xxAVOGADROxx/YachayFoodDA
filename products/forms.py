from django import forms
class ProductsApplyForm(forms.Form):
    code = forms.CharField()
