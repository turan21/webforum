from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import AuthorRegisterViewSet, AuthorCreateListView, AuthorRetrieveUpdateDestroyAPIView


urlpatterns = [
     path('register/', AuthorRegisterViewSet.as_view()),
     path('', AuthorCreateListView.as_view()),
     path('<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

     path('token/', TokenObtainPairView.as_view()),
     path('token/refresh/', TokenRefreshView.as_view()),
]
