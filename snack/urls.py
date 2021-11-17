from .views import SnackListView,SnackDetailView,SnackCreateView,SnackUpdateView,SnackDeleteView
from django.urls import path

urlpatterns=[
    path("snack_list",SnackListView.as_view(),name='snack_list'),
    path("snack_list/<int:pk>/",SnackDetailView.as_view(),name='snack_detail'),
    path("snack_list/create/",SnackCreateView.as_view(),name='snack_create'),
    path("snack_list/<int:pk>/update/",SnackUpdateView.as_view(),name='snack_update'),
    path("snack_list/<int:pk>/delete/",SnackDeleteView.as_view(),name='snack_delete'),
]