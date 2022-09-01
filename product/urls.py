from django.urls import path,include

from product import views



urlpatterns = [
    path('products/', views.ProductsList.as_view()),
    path('products/<str:name>/', views.ProductDetail.as_view()),
    path('carts', views.ListCart.as_view(), name='allcarts'),
    path('carts/<int:pk>', views.DetailCart.as_view(), name='cartdetail'),
    path('orders', views.ListOrder.as_view(), name='allorders'),
    path('orders/<int:pk>', views.DetailOrder.as_view(), name='orderdetail'),
    path('users', views.UserList.as_view(), name='userlist'),

]