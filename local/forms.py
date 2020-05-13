from django import forms
from django.shortcuts import get_object_or_404, get_list_or_404
from local.models import Category, Product 


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Category's Name"})
    )

    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Product's Name"})
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all().order_by('name'),
        empty_label="Select a Category"
    )

    CHOICES = ((True, 'Yes'), (False, 'No'))

    class Meta:
        model = Product
        labels = {
            'name': 'Product Name',
            'is_indian': 'Indian Product?'
        }
        fields = '__all__'
        widgets = {
            'is_indian': forms.Select(choices=((True, 'Yes'), (False, 'No')))
        }
        

class SearchProductForm(forms.Form):

    product = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Product's Name"})
    )

    def save(self, product_name):
        products = Product.objects.filter(name=product_name.title())
        if not products.exists():
            products = Product.objects.filter(name__icontains=product_name.title())

        return products


class BrowseCategoryForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all().order_by('name'),
        empty_label="Select a Category"
    )
    manufacturer = forms.ChoiceField(
        choices=(
            (True, "Indian"),
            (False, "All")
        )
    )

    def save(self, category_name, is_only_indian):
        category = Category.objects.get(name=category_name)
        products = Product.objects.filter(
            category=category, 
        ).order_by('name')
        if is_only_indian:
            products = products.filter(is_indian=is_only_indian)
        return dict(
            category=category, 
            products=products, 
            is_only_indian=is_only_indian
        )
