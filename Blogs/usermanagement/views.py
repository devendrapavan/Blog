from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework import generics


class SignUpManagement(generics.GenericAPIView):

    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny, ]

    def post(self, request):
        try:
            data = self.serializer_class(data=request.data)
            if data.is_valid() is False:
                return Response({'error':'bad request'}, status=status.HTTP_400_BAD_REQUEST)
            if CustomUserManager().is_user_exists(data.validated_data.get("email")):
                return Response({"error": "User already exists"}, status=status.HTTP_207_MULTI_STATUS)


            USERMODEL = get_user_model()
            new_user = USERMODEL.objects.create_user_custom(
                data.validated_data.get("email"),
                data.validated_data.get("password"),
                data.validated_data.get("first_name"),
                data.validated_data.get("last_name"),
                data.validated_data.get("is_staff"),
            )
            if new_user:
                user_model = get_user_model()
                # login(request, auth_user)
                user = user_model.objects.get(email=data.validated_data.get("email"))
                return Response({"email": user.email},
                                status=status.HTTP_201_CREATED)
            else:
                return Response(data.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            # logger.error(ExceptionLoggingMiddleware().process_exception(), exc_info=True)
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetUserInfo(generics.GenericAPIView):

    def post(self, request):
        user = request.user
        return Response({
            "email":user.email,
            "staff":user.is_staff,
            "id":user.id
        }, status=status.HTTP_200_OK)