from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ['name', 'description', 'preview', 'category', 'price']

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        for word in self.forbidden_words:
            if word in name:
                raise forms.ValidationError(f"Нельзя использовать слово '{word}' в названии продукта.")
        return name

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        for word in self.forbidden_words:
            if word in description:
                raise forms.ValidationError(f"Нельзя использовать слово '{word}' в описании продукта.")
        return description
