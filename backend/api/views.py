from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    RegisterSerializer,
    CircleSerializer,
    JoinCircleSerializer,
)

from .models import Circle, CircleMember, Round
from .serializers import RegisterSerializer, CircleSerializer
from .models import Circle, CircleMember, Round, Contribution

from .serializers import (
    RegisterSerializer,
    CircleSerializer,
    JoinCircleSerializer,
    ContributionSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]



class ContributeView(APIView):

    def post(self, request, round_id):

        try:
            round_obj = Round.objects.get(id=round_id)
        except Round.DoesNotExist:
            return Response({"error": "Round not found"}, status=404)

        serializer = ContributionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        if Contribution.objects.filter(
            round=round_obj,
            member=request.user
        ).exists():

            return Response(
                {"error": "Already contributed"},
                status=400
            )

        contribution = Contribution.objects.create(
            round=round_obj,
            member=request.user,
            amount=serializer.validated_data["amount"]
        )

        return Response(
            {
                "message": "Contribution successful",
                "amount": contribution.amount
            },
            status=201
        )





class JoinCircleView(APIView):

    def post(self, request):

        serializer = JoinCircleSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        invite_code = serializer.validated_data["invite_code"]

        try:
            circle = Circle.objects.get(invite_code=invite_code)
        except Circle.DoesNotExist:
            return Response(
                {"error": "Circle not found"},
                status=404
            )

        if CircleMember.objects.filter(
            circle=circle,
            user=request.user
        ).exists():

            return Response(
                {"error": "Already a member"},
                status=400
            )

        member_count = CircleMember.objects.filter(circle=circle).count()

        if member_count >= 4:
            return Response(
                {"error": "Circle is full"},
                status=400
            )

        CircleMember.objects.create(
            circle=circle,
            user=request.user,
            rotation_position=member_count + 1
        )

        return Response({
            "message": "Joined successfully",
            "rotation_position": member_count + 1
        })

class CreateCircleView(APIView):

    def post(self, request):
        serializer = CircleSerializer(data=request.data)

        if serializer.is_valid():

            # Create the circle
            circle = serializer.save(admin=request.user)

            # Add creator as first member
            CircleMember.objects.create(
                circle=circle,
                user=request.user,
                rotation_position=1
            )

            # Automatically create Round 1
            Round.objects.create(
                circle=circle,
                recipient=request.user,
                round_number=1
            )

            return Response(
                {
                    "message": "Circle created successfully",
                    "circle": CircleSerializer(circle).data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    