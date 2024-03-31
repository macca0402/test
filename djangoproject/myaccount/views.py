from django.contrib.auth import authenticate, login
from rest_framework import status, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserCreateSerializer, UserSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


@permission_classes([AllowAny,])
class LoginAPI(KnoxLoginView):

    # def post(self,request,format=None):
    #     serializer = AuthTokenSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         user = serializer.validated_data['user']
    #         login(request,user)
    #         response=super().post(request,format=None)
    #     else:
    #         return Response({'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(response.data,status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = serializer.validated_data.get("user")
        login(request, serializer)
        return super(LoginAPI, self).post(request, format=None)


@api_view(["POST"])
def user_logout(request):
    if request.user.is_authenticated:
        # Xóa token xác thực của người dùng hiện tại
        request.auth.delete()
        return Response({"detail": "Logged out successfully."}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"detail": "User is not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)
