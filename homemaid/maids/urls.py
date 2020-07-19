from django.urls import path

from .views import (
    MaidAddView,
    MaidListView,
    maid_another_list_view,
    MaidListAPIView,
)


urlpatterns = [
    path('', MaidListView.as_view(), name='maid-list'),
    path('api/', MaidListAPIView.as_view(), name='maid-list-api'),
    path('add/', MaidAddView.as_view(), name='maid-add'),
    path('v2/', maid_another_list_view, name='maid-another-list'),
]
