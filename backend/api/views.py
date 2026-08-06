from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import Sum

from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Circle,
    CircleMember,
    Round,
    Contribution,
    Payout,
)

from .serializers import (
    RegisterSerializer,
    CircleSerializer,
    JoinCircleSerializer,
    ContributionSerializer,
)



# Register

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]



# Create Circle

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

            Round.objects.create(
                circle=circle,
                recipient=request.user,
                round_number=1,
                status="OPEN"
            )

            return Response(
                {
                    "message": "Circle created successfully",
                    "circle": CircleSerializer(circle).data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



# Join Circle

class JoinCircleView(APIView):

    def post(self, request):

        serializer = JoinCircleSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        invite_code = serializer.validated_data["invite_code"]

        try:
            circle = Circle.objects.get(invite_code=invite_code)
        except Circle.DoesNotExist:
            return Response(
                {"error": "Circle not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if CircleMember.objects.filter(
            circle=circle,
            user=request.user
        ).exists():

            return Response(
                {"error": "Already a member"},
                status=status.HTTP_400_BAD_REQUEST
            )

        member_count = CircleMember.objects.filter(
            circle=circle
        ).count()

        if member_count >= 4:
            return Response(
                {"error": "Circle is full"},
                status=status.HTTP_400_BAD_REQUEST
            )

        CircleMember.objects.create(
            circle=circle,
            user=request.user,
            rotation_position=member_count + 1
        )

        return Response(
            {
                "message": "Joined successfully",
                "rotation_position": member_count + 1
            },
            status=status.HTTP_201_CREATED
        )



# Contribute

class ContributeView(APIView):

    def post(self, request, round_id):

        try:
            round_obj = Round.objects.get(id=round_id)
        except Round.DoesNotExist:
            return Response(
                {"error": "Round not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ContributionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        if Contribution.objects.filter(
            round=round_obj,
            member=request.user
        ).exists():

            return Response(
                {"error": "Already contributed"},
                status=status.HTTP_400_BAD_REQUEST
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
            status=status.HTTP_201_CREATED
        )



# Approve Payout

class ApprovePayoutView(APIView):

    @transaction.atomic
    def post(self, request, round_id):

        try:
            round_obj = Round.objects.select_for_update().get(id=round_id)
        except Round.DoesNotExist:
            return Response(
                {"error": "Round not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if round_obj.circle.admin != request.user:
            return Response(
                {"error": "Only the admin can approve payouts"},
                status=status.HTTP_403_FORBIDDEN
            )

        if round_obj.status == "CLOSED":
            return Response(
                {"error": "Round already closed"},
                status=status.HTTP_400_BAD_REQUEST
            )

        members = CircleMember.objects.filter(circle=round_obj.circle)
        contributions = Contribution.objects.filter(round=round_obj)

        if contributions.count() != members.count():
            return Response(
                {"error": "Not all members have contributed"},
                status=status.HTTP_400_BAD_REQUEST
            )

        total = contributions.aggregate(
            total=Sum("amount")
        )["total"] or 0

        Payout.objects.create(
            round=round_obj,
            recipient=round_obj.recipient,
            total_amount=total
        )

        round_obj.status = "CLOSED"
        round_obj.save()

        next_position = round_obj.round_number + 1

        next_member = CircleMember.objects.filter(
            circle=round_obj.circle,
            rotation_position=next_position
        ).first()

        if next_member:
            Round.objects.create(
                circle=round_obj.circle,
                recipient=next_member.user,
                round_number=next_position,
                status="OPEN"
            )

        return Response(
            {
                "message": "Payout approved successfully",
                "total_paid": total
            },
            status=status.HTTP_200_OK
        )