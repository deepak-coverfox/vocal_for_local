from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from local import urls as local_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(
        template_name="local/base.html"), 
    ),
    re_path(r"", include((local_urls, "local"), namespace="local")),
]
