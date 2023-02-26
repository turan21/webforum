from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import ForumPermission, CommentPermission
from .serializers import ForumSerializer, CommentSerializer
from .models import Forum, Comment


class ForumPagePagination(PageNumberPagination):
    page_size = 3


class ForumViewSet(generics.ListCreateAPIView):
    """
        API для просмотра и создания Форума
    """
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
    permission_classes = [ForumPermission, ]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', ]
    search_fields = ['title', ]
    ordering_fields = ['title', ]
    pagination_class = ForumPagePagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class ForumRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
        API для детального просмотра, изменения и удаления Форума
    """
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
    permission_classes = [ForumPermission, ]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    """
        API для просмотра и создания комментариев к Форуму
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = ForumPagePagination
    permission_classes = [CommentPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(forum_id=self.kwargs.get('forum_id'))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author,
            forum_id=self.kwargs.get('forum_id')
        )


class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
        API для детального просмотра, изменения и удаления комментариев
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(forum_id=self.kwargs.get('forum_id'))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author,
            forum_id=self.kwargs.get('forum_id')
        )
