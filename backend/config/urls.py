from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import include

from users.views import jwt_exchange





# Base URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/google/exchange/", jwt_exchange),
    path("accounts/", include("allauth.urls")),
]


urlpatterns += [
    path("api/users/", include("users.urls")),
]

# Posts URLs
urlpatterns += [
    path("api/posts/", include("posts.urls")),
]

# Social URLs
urlpatterns += [
    path("api/social/", include("social.urls")),
]