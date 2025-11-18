from django.urls import path  
from . import views

app_name = "food"
urlpatterns =[
    path("", views.IndexListView.as_view(), name="index"), #type:ignore
    path("<int:pk>", views.ItemDetailView.as_view(), name="detail"), 
    
    path("add", views.CreateItemView.as_view(), name="add_item"),
    path("update/<int:id>", views.update_item, name="update_item"),
    path("delete/<int:id>/", views.delete_item, name="delete_item"),
]