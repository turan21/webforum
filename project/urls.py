from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Web Forum API",
      default_version='v-0.1',
      description="API для взаимодействия с Web Forum API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="DadyaEblan@gmail.com"),
      license=openapi.License(name="No Licence"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include([
        path('account/', include('accounts.urls')),
        path('forum/', include('web_forum.urls')),
        ])),

    # documentation URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_doc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_doc'),
]
