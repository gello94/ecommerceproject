"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_products, name='index'),
    path('accounts/', include(urls_accounts)),
    path('products/', include(urls_products)),
    path('cart/', include(urls_cart)),
    path('checkout/', include(urls_checkout)),
    path('search/', include(urls_search)),
    re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
