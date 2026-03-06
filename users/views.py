from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import User
from .serializers import UserSerializer, RegisterUserSerializer
from .permissions import IsAdminUserRole


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated, IsAdminUserRole]

    def get_serializer_class(self):

        if self.action == "create":
            return RegisterUserSerializer

        return UserSerializer

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):

        serializer = UserSerializer(request.user)

        return Response(serializer.data)