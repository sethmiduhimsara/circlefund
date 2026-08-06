from django.contrib import admin
from .models import Circle, CircleMember, Round
from .models import (
    Circle,
    CircleMember,
    Round,
    Contribution,
)

admin.site.register(Circle)
admin.site.register(CircleMember)
admin.site.register(Round)
admin.site.register(Contribution)