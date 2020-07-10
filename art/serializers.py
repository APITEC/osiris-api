from rest_framework.serializers import ModelSerializer
from art.models import Piece, Transaction


class PieceSerializer(ModelSerializer):
    class Meta:
        model = Piece
        fields = '__all__'


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
