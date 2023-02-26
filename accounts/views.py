from rest_framework import generics, viewsets
from .models import Author
from .permissions import AuthorPermission
from .serializers import AuthorRegisterSerializer


class AuthorRegisterViewSet(generics.CreateAPIView):
    """
        API для регистрации пользователей
    """
    serializer_class = AuthorRegisterSerializer
    queryset = Author.objects.all()


class AuthorCreateListView(generics.ListCreateAPIView):
    """
        API для просмотра пользователей
    """
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer


class AuthorRetrieveUpdateDestroyAPIView(viewsets.ModelViewSet):
    """
        API для детального просмотра, изменения и удаления пользователей
    """
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer
    permission_classes = [AuthorPermission, ]
