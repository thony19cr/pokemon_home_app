from django.urls import path
from . import views

urlpatterns = [
    path("owner_list/", views.list_owner, name="owner_list"),
    path("owner_search/", views.owner_search, name="owner_search"),
    path("owner_details/", views.owner_details, name="owner_detail"),

    path("owner_create/", views.owner_create, name="owner_create"),
    path("owner_delete/<int:id_owner>", views.owner_delete, name="owner_delete"),
    path("owner_update/<int:id_owner>", views.owner_edit, name="owner_update"),

    # URLs para las vistas basadas en clases
    path("owner_list_vc/", views.OwnerList.as_view(), name="owner_list_vc"),
    path("owner_edit_vc/<int:pk>", views.OwnerUpdate.as_view(), name="owner_edit_vc"),
    path("owner_delete_vc/<int:pk>", views.OwnerDelete.as_view(), name="owner_delete_vc"),
]
