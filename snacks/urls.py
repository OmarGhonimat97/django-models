from django.urls import path

from .views import HomePage, SnackListView, SnackDetailView

urlpatterns = [
    # path('', HomePage.as_view(), name='home'),
    path('', SnackListView.as_view(), name='snacks_list'),
    path('snacks/<int:pk>', SnackDetailView.as_view(), name='snack_detail'),
]
