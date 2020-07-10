from rest_framework.viewsets import ModelViewSet
from art.models import Piece, Transaction
from art import serializers


# Create your views here.
class Piece(ModelViewSet):
    queryset = Piece.objects.all()
    serializer_class = serializers.PieceSerializer


class Transaction(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = serializers.PieceSerializer
