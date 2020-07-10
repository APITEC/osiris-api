from rest_framework.viewsets import ModelViewSet
from users.models import User
from users import serializers


# Create your views here.
class User(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
