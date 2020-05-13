from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse

from local.models import Category, Product
from local.forms import ( 
    SearchProductForm, BrowseCategoryForm,
    ProductForm, CategoryForm
)


def add_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'local/ty_note.html') 
    return render(request, 'local/add_category.html', {'form': form})


def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'local/ty_note.html')
    return render(request, 'local/add_product.html', {'form': form})


class SearchProductView(View):
    
    template = 'local/search_product.html'

    def get(self, request, *args, **kwargs):
        form = SearchProductForm()
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        context = {'is_clicked' : True}
        form = SearchProductForm(request.POST)
        context.update({'form': form})
        if form.is_valid():
            product_name = form.cleaned_data.get("product")
            products = form.save(product_name=product_name)
            context.update({"products": products})
        return render(request, self.template, context)


class BrowseCategoryView(View):
    
    template = 'local/browse_category.html'

    def get(self, request, *args, **kwargs):
        form = BrowseCategoryForm()
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        context = {'is_clicked': True}
        form = BrowseCategoryForm(request.POST)
        context.update({'form': form})
        if form.is_valid():
            category_name = form.cleaned_data.get("category")
            is_only_indian = eval(form.cleaned_data.get('manufacturer'))
            context.update(form.save(
                category_name=category_name,
                is_only_indian=is_only_indian
            ))
        return render(request, self.template, context)
