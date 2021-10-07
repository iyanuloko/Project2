from django import forms
from .models import RiskRegister, Category, Severity, RSev

class DateInput(forms.DateInput):
    input_type = 'date'

class RiskRegisterForm(forms.ModelForm):
    class Meta:
        model = RiskRegister
        fields = ['date', 'category', 'explanation', 'roles']
        widgets = {
            'date': DateInput(),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

class SeverityForm(forms.ModelForm):
    class Meta:
        model = Severity
        fields = ['roles']

class RSevForm(forms.ModelForm):
    class Meta:
        model = RSev
        fields = ['severity']
#'is_regulatory', 'is_legal', 'is_reputational', 'is_liquidity','explanation' 'is_none','date_response'
