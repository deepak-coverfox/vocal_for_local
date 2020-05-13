from django.urls import path
from django.views.generic import TemplateView
from local import views

urlpatterns = [
    path("", TemplateView.as_view(
        template_name="local/base.html"), 
        name="home"
    ),
    path(
        "search-product", 
        views.SearchProductView.as_view(), 
        name="search_product"
    ),
    path(
        "browse-category", 
        views.BrowseCategoryView.as_view(), 
        name="browse_category"
    ),
    path(
        "modify-category", 
        views.add_category, 
        name="modify_category"
    ),
    path(
        "modify-product", 
        views.add_product, 
        name="modify_product"
    ),
]