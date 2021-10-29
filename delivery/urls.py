from django.urls import path
from .views import *
urlpatterns = [
    path('delivery/', OrderListView.as_view()),
    path('delivery/<int:pk>/', OrderDetailView.as_view()),
]
