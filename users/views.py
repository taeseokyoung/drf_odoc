from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate, login

from users.models import User
from users.serializers import UserSerializer
# Create your views here.


class UserView(APIView):

    def get(self, request):
        # 직렬화(json)된 사용자 정보 return
        # user = request.user
        # return Response(UserSerializer(user).data)
        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)

    def post(self, request):
        print(request.data)
        # 시리얼라이저 사용하지 않을 시
        # User.objects.create(**request.data)
        # 시리얼라이저 사용 시
        serializer = UserSerializer(data=request.data)

        # 유효성 검사
        # case 1
        serializer.is_valid(raise_exception=True)
        # case 2
        # if not serializer.is_valid():
        #     return Response({"error": serializer.errors}, status=400)

        # serializers.py 의 validate 함수 실행

        # 검증, serializers.py 의 create 함수 실행
        serializer.save()

        return Response({"message": "user post"})

    def put(self, request):
        return Response({"message": "user put"})

    def delete(self, request):
        return Response({"message": "user delete"})


class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(request, **request.data)
        if not user:
            return Response({"error": "유효하지 않은 사용자"})

        login(request, user)
        return Response({"message": "로그인 성공"})
