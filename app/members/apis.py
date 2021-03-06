from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from items.models import Item
from .models import LikeItem
from .serializers import SiteAuthTokenSerializer, SocialAuthTokenSerializer, SiteSigunUpSerializer, \
    LikeItemCreateDestroySerializer, LikeItemListSerializer
from .serializers import UserSerializer

User = get_user_model()


# 회원 가입시 동일 ID 있는지 check
class SignUpCheckIDView(APIView):
    def post(self, request, format=None):
        username = request.POST.get('username')
        if not username:
            data = {'error': 'username 값이 없습니다'}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        user_exist = User.objects.filter(username=username).exists()
        if user_exist:
            # 같은 ID가 존재함
            data = {'error': '동일한 username이 존재합니다'}
        else:
            data = {'pass': '사용가능한 username입니다'}
        return Response(data, status=status.HTTP_200_OK)


# 회원 가입
class SiteSignUpAPIView(APIView):
    def post(self, request, format=None):
        serializer = SiteSigunUpSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 로그인시 token 발행
class SiteAuthTokenAPIView(APIView):
    def post(self, request, format=None):
        serializer = SiteAuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# social 로그인 시 token 발행
class SocialAuthTokenAPIView(APIView):

    def post(self, request, format=None):
        serializer = SocialAuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# token에 대한 user 정보
class UserView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request, format=None):
        user = request.user
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)


# 찜하기 기능
class LikeItemListCreateDestroyView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request):
        like_items = LikeItem.objects.filter(user=request.user)
        serializer = LikeItemListSerializer(like_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        item_pk = request.data.pop('item_pk')
        serializer = LikeItemCreateDestroySerializer(
            data={
                'item': item_pk
            },
            context={'request': request},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        item = get_object_or_404(Item, pk=request.data.get('item_pk'))
        like_item = get_object_or_404(
            LikeItem, item=item, user=request.user)
        like_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

