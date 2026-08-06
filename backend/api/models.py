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