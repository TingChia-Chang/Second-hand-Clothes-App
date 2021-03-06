from django.urls import path
from . import views
app_name = 'second_hand_clothes_app'
urlpatterns = [
    #clothes views
    path('', views.clothes_index, name="clothes_index"),
    path('list/', views.clothes_list, name="clothes_list"),
    path('list/sort_by_price', views.clothes_sort, name="clothes_sort"),
    path('list/add_comment', views.clothes_add_comment, name="clothes_add_comment"),
    path('list/delete_comment', views.clothes_delete_comment, name="clothes_delete_comment"),
    path('list/<int:item_id>', views.clothes_detail, name="clothes_detail"),
    path('list/<int:item_id>/edit', views.clothes_edit, name="clothes_edit"),
    path('list/<int:item_id>/delete', views.clothes_delete, name="clothes_delete"),
    path('add_item/', views.clothes_add_item, name="clothes_add_item"),
    path('search_result/', views.clothes_search_result, name="clothes_search_result"),
    path('sign_in/', views.clothes_sign_in, name="clothes_sign_in"),
]