from django.urls import path
from . import views

urlpatterns = [
    path("owner_list/", views.list_owner, name="owner_list"),
    path("owner_search/", views.owner_search, name="owner_search"),
    path("owner_details/", views.owner_details, name="owner_detail"),

    path("owner_create/", views.owner_create, name="owner_create"),
]
