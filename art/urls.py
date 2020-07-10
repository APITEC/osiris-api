from django.urls import path
from art import views

urlpatterns = [
    path('piece/', views.Piece.as_view({'get': 'list', 'post': 'create', 'patch': 'partial_update'})),
    path('transaction/', views.Transaction.as_view({'get': 'list', 'post': 'create', 'patch': 'partial_update'})),
]