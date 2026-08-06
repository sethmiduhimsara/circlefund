from django.db import models
from django.contrib.auth.models import User
import uuid


class Circle(models.Model):
    name = models.CharField(max_length=100)

    invite_code = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="admin_circles"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CircleMember(models.Model):
    circle = models.ForeignKey(
        Circle,
        on_delete=models.CASCADE,
        related_name="members"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rotation_position = models.PositiveSmallIntegerField()

    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("circle", "user")
        ordering = ["rotation_position"]

    def __str__(self):
        return f"{self.user.username} - {self.circle.name}"


class Round(models.Model):

    STATUS_CHOICES = [
        ("OPEN", "OPEN"),
        ("PENDING_APPROVAL", "PENDING_APPROVAL"),
        ("CLOSED", "CLOSED"),
    ]

    circle = models.ForeignKey(
        Circle,
        on_delete=models.CASCADE
    )

    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    round_number = models.PositiveIntegerField()

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="OPEN"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Round {self.round_number}"


class Contribution(models.Model):

    round = models.ForeignKey(
        Round,
        on_delete=models.CASCADE,
        related_name="contributions"
    )

    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    contributed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("round", "member")

    def __str__(self):
        return f"{self.member.username} - Round {self.round.round_number}"