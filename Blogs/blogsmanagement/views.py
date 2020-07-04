from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework import generics

class CreateArticle(generics.GenericAPIView):

    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):

        try:
            data = self.serializer_class(data=request.data)
            if data.is_valid() is False:
                return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
            user = request.user
            if user.is_staff == True:
                status_code = 'APPROVED'
            else:
                status_code = 'CREATED'
            data.save_article(data.validated_data, user, status_code)
            return Response("success", status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateArticle(generics.GenericAPIView):

    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        try:
            data = self.serializer_class(data=request.data)
            if data.is_valid() is False:
                return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
            user = request.user
            if user.is_staff:
                status_code = 'APPROVED'
                data.update_article(data.validated_data, user, status_code)
            else:
                status_code = 'CREATED'
                data.update_article(data.validated_data, user, status_code)
            return Response("success", status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetBlogs(generics.GenericAPIView):
    serializer_class = ArticleDataSerializer
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        try:
            if request.user.is_staff:
                return  Response(self.serializer_class(Article.objects.all(),many=True).data, status= status.HTTP_200_OK)
            return Response(self.serializer_class(Article.objects.filter(created_by=request.user),many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetArticleById(generics.GenericAPIView):
    serializer_class = ArticleDataSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request,id):
        try:

            if request.is_staff:
                return Response(self.serializer_class(Article.objects.filter(id=id).first()).data, status=status.HTTP_200_OK)
            return Response(self.serializer_class(Article.objects.filter(created_by=request.user,id=id).first()).data,
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetApprovedArticleById(generics.GenericAPIView):
    serializer_class = ArticleDataSerializer
    def get(self,request,id):
        return Response(self.serializer_class(Article.objects.filter(id=id).first()).data,
                        status=status.HTTP_200_OK)

class GetALlApprovedArticles(generics.ListAPIView):
    queryset = Article.objects.filter(status='APPROVED')
    serializer_class = ArticleDataSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
