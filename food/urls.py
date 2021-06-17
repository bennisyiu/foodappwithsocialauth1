from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
    # index page: /food/
    path('', views.index, name="index"),
    # show page: /food/1 (id)
    path('<int:item_id>/', views.detail, name="detail"),
    path('item/', views.item, name="item"),
    # add items
    path('add', views.create_item, name="create_item"),
    # edit items
    path('update/<int:id>/', views.update_item, name="update_item"),
    # delete itema
    path('delete/<int:id>/', views.delete_item, name="delete_item"),

]
