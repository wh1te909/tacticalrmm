from django.urls import path
from . import views

urlpatterns = [
    path("installer/<client>/sites/", views.installer_list_sites),
    path("listclients/", views.list_clients),
    path("listsites/", views.list_sites),
    path("installer/listclients/", views.installer_list_clients),
    path("addclient/", views.add_client),
    path("editclient/", views.edit_client),
    path("addsite/", views.add_site),
    path("editsite/", views.edit_site),
    path("loadtree/", views.load_tree),
    path("loadclients/", views.load_clients),
    path("initialsetup/", views.initial_setup),
]
