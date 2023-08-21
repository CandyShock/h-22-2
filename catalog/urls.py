from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, sing_in, ProductCreateView, ProductUpdateView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', cache_page(60)(ProductListView.as_view()), name='home'),
    path('contact/', sing_in, name='sing_in'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
]
