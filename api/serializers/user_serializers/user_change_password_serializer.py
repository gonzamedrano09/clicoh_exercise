from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserChangePasswordSerializer(serializers.ModelSerializer):

    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get("password"))
        return instance

    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name"]
