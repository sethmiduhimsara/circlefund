from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Circle, CircleMember
from .serializers import RegisterSerializer, CircleSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class CreateCircleView(APIView):

    def post(self, request):
        serializer = CircleSerializer(data=request.data)

        if serializer.is_valid():

            circle = serializer.save(admin=request.user)

            CircleMember.objects.create(
                circle=circle,
                user=request.user,
                rotation_position=1
            )

            return Response(
                CircleSerializer(circle).data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=400)