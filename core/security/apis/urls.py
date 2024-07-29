from django.urls import path
from core.security.apis import api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

urlpatterns = [
    # login logout
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),  # logout
    # fin login logout
    # pruebas
    path('test/', api.test, name='test_security'),  # prueba de api
    path('test_token/', api.test_token, name='test_token')  # prueba de token
    # fin pruebas
]
