from django import forms


class ProductSearchForm(forms.Form):  
  q = forms.CharField(required=False, label='Search')
  min_price = forms.DecimalField(required=False, decimal_places=2, max_digits=10)
  max_price = forms.DecimalField(required=False, decimal_places=2, max_digits=10)