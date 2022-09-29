from django.urls import path
from . import views


app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("created/", views.create2, name="created"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),
    path("updated/<int:pk>", views.updated, name="updated"),
    path("update2/<int:pk>", views.update2, name="update2"),
    path("test/", views.test, name="test"),
]
