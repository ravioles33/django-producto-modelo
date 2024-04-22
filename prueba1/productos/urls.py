from django.urls import path
from productos import views

urlpatterns = [
    path('list/', views.ProductoListView.as_view(), name='producto_list'),
    path('detail/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),
]
