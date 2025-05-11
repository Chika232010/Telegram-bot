
from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.category_list, name='category_list'), 
    path('<slug:slug>/', views.category_detail, name='category_detail'),  
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]
