from django.urls import path
from . import views
app_name = 'second_hand_clothes_app'
urlpatterns = [
    #clothes views
    path('', views.clothes_index, name="clothes_index"),
    path('list/', views.clothes_list, name="clothes_list"),
    path('list/<int:item_id>', views.clothes_detail, name="clothes_detail"),
    path('add_item/', views.clothes_add_item, name="clothes_add_item"),
    path('edit/', views.clothes_edit, name="clothes_edit"),
    path('search_result/', views.clothes_search_result, name="clothes_search_result"),
    path('sign_in/', views.clothes_sign_in, name="clothes_sign_in"),
    path('sign_in_action', views.sign_in, name="sign_in"),
    path('log_out/', views.log_out, name="log_out"),
]