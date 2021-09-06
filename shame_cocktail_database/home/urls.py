from django.urls import path
from .views import (
    DrinksListView, 
    DrinksDetailView,
    DrinksCreateView,
    DrinksUpdateView)


urlpatterns = [
    path('', DrinksListView.as_view(), name='home'),
    path('drink/<int:pk>/', DrinksDetailView.as_view(), name='drinks-detail'),
    path('drink/new/', DrinksCreateView.as_view(), name='drinks-create'),
    path('drink/<int:pk>/update', DrinksUpdateView.as_view(), name='drinks-update'),
]
