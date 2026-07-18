from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('viewproducts/', views.viewproducts, name='viewproducts'),
    path('dproduct/<int:id>/', views.dproduct, name='dproduct'),
    path('editproduct/<int:id>/', views.editproduct, name='editproduct')
]