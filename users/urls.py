from django.urls import path
from users import views

urlpatterns = [
    path('', views.User.as_view({'get': 'list', 'post': 'create', 'patch': 'partial_update'})),
]