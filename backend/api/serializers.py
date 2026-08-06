from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Circle, Contribution


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circle
        fields = [
            "id",
            "name",
            "invite_code",
            "created_at",
        ]
        read_only_fields = ["invite_code", "created_at"]


class JoinCircleSerializer(serializers.Serializer):
    invite_code = serializers.UUIDField()


class ContributionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contribution
        fields = ["amount"]