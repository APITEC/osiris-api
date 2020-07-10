from django.urls import path
from art import views

urlpatterns = [
    path('piece/', views.Piece.as_view()),
    path('transaction/', views.Transaction.as_view()),
]