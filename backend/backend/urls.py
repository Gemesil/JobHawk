from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jobsearch.urls')),
    path('saml2/', include('djangosaml2.urls')),
    re_path(r'^.*', TemplateView.as_view(template_name="index.html")),
]
