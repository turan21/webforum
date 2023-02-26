from django.urls import path
from .views import ForumViewSet, ForumRetrieveUpdateDestroy, CommentListCreateAPIView, CommentRetrieveUpdateDestroy

urlpatterns = [
    path('', ForumViewSet.as_view()),
    path('<int:pk>/', ForumRetrieveUpdateDestroy.as_view()),

    path('<int:forum_id>/comments/', CommentListCreateAPIView.as_view()),
    path('<int:forum_id>/comments/<int:pk>/', CommentRetrieveUpdateDestroy.as_view()),
]
