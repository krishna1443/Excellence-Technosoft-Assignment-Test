from rest_framework import serializers
from .models import Candidate, TestScore
from django.contrib.auth.models import User

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'email', 'address']

class TestScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestScore
        fields = ['id', 'candidate', 'test_name', 'score']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user