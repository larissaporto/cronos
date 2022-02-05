from rest_framework import serializers
from .models import TeamMember

JOB_CHOICES = (
    ("1", "Database Analyst"),
    ("2", "Backup Analyst"),
    ("3", "Backend Developer"),
    ("4", "Frontend Developer"),
    ("5", "FullStack Developer"),
)

class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    job_title = serializers.ChoiceField(choices=JOB_CHOICES)

    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'job_title']