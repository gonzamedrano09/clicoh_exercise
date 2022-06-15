from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from api.serializers.user_serializers.user_serializer import UserSerializer
from api.serializers.user_serializers.user_change_password_serializer import UserChangePasswordSerializer


User = get_user_model()


class UserViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin):

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [AllowAny]
        return super(UserViewSet, self).get_permissions()

    def get_serializer_class(self):
        if self.action == "change_password":
            return UserChangePasswordSerializer
        return UserSerializer

    def get_object(self):
        return self.request.user

    @action(detail=False, url_path="change-password", methods=["post"])
    def change_password(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
