from django.contrib.auth.models import User
from projects.models import Project
from rest_framework import serializers

class Projectser(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'details', 'totalTarget', 'startproject', 'endproject', 'category']