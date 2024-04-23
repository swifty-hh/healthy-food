from django.contrib import admin
from .models import *

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
  list_display=('follower', 'following', 'created_at')