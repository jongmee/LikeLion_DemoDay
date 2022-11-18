from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create(validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user # 유저를 암호화해서 저장 

    class Meta:
        model = User
        fields = ['pk', 'username', 'password']