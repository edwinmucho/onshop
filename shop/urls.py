from django.urls import path
from .views import *

app_name = "shop"

urlpatterns = [
    path('', product_in_category, name="product_all"),
    path('<category_slug>/', product_in_category, name="product_in_category"),
    path('<int:id>/<product_slug>/', product_detail, name="product_detail"),
]
