from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from .serializers import MeSerializer


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(MeSerializer(request.user).data)


@login_required
def jwt_exchange(request):
    user = request.user
    refresh = RefreshToken.for_user(user)
    return JsonResponse({
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    })