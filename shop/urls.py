from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('my/', views.my_products, name='my_product_list'),
    path('my/<slug:category_slug>/', views.my_products, name='my_product_list_by_category'),

    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),

    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('my/<int:id>/<slug:slug>/', views.my_product_detail, name='my_product_detail'),
    path('my/<int:id>/edit/meva/', views.my_product_edit, name='my_product_edit'),
    path('my/<int:id>/delete/meva/', views.my_product_delete, name='my_product_delete'),
    path('my/create/product/', views.my_product_create, name='my_product_create'),
    path('buyurtmalar/list/me/', views.my_order_list, name='my_order_list'),
    path('buyurtmani/qabulqilish/<int:id>/me/', views.my_order_accept, name='my_order_accept'),
    path('buyurtmani/reject/<int:id>/me/', views.my_order_reject, name='my_order_reject'),
    # path('list/<slug:category_slug>/', views.MyClassView.as_view(), name='product_list'),
]
