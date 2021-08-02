from .tokens import get_refresh_token, get_access_token
from .serializers import LoginEmailSerializer
from rest_framework.viewsets import ViewSet
from django.contrib.auth import authenticate
from rest_framework.response import Response


class LoginView(ViewSet):
    """
    for login user by post request and save object to Jwt model
    """
    serializer_class = LoginEmailSerializer

    def create(self, request):
        """
        save access and refresh token in Jwt model with post request
        :param request: for user Identification
        :return: login user
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data.get('email'),
                            password=serializer.validated_data.get('password'))
        if not user:
            return Response({"error": "Invalid email or password"}, status=400)

        access = get_access_token({"user_id": user.id})
        refresh = get_refresh_token()

        return Response({"access": access, "refresh": refresh})
