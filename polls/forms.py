from typing import Any, Dict
from django import forms

from polls.models import RandomGenerator, AdvanceRandomGenerator

# Create your views here.

class RandomGeneratorForm(forms.ModelForm):
    class Meta:
        model = RandomGenerator
        fields = ('from_number', 'to_number', 'count')
        widgets = {
            'from_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'to_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.result_list = list(instance.generate(instance.count))
        if commit:
            instance.save()
        return instance
    
    def clean(self) -> Dict[str, Any]:
        if self.cleaned_data['from_number'] > self.cleaned_data['to_number']:
            raise forms.ValidationError('From number must be less than to number')
        return super().clean()

class AdvanceRandomGeneratorForm(RandomGeneratorForm):
    class Meta:
        model = AdvanceRandomGenerator
        fields = ('from_number', 'to_number', 'count')
        widgets = {
            'from_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'to_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.generator_type = RandomGenerator.GeneratorChoices.ADVANCED
        if commit:
            instance.save()
        return instance

    def clean(self) -> Dict[str, Any]:
        if self.cleaned_data['from_number'] < 1:
            raise forms.ValidationError('From number must be greater than 0')
        if self.cleaned_data['to_number'] < 1:
            raise forms.ValidationError('To number must be greater than 0')
        return super().clean()