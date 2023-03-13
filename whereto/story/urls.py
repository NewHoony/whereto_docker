from django.urls import path
from . import views

app_name = "story"

urlpatterns = [

    path('index/', views.BookListView.as_view(), name="index"),
    path("delete_book/<pk>", views.delete_book, name="delete_book"),
    path("index/create/", views.UploadBookView.as_view(), name="create"),
]