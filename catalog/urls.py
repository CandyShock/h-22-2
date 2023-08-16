from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, sing_in, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contact/', sing_in, name='sing_in'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product')
]
