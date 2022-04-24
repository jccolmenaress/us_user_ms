from  un_user_ms.models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =['id', 'email', 'name', 'status', 'description']

