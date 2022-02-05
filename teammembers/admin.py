from django.contrib import admin
from .models import TeamMember
# Register your models here.

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'job_title')