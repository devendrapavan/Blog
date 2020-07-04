from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(required=False)

    class Meta:
        model = Article
        fields = ('id', 'header', 'body', 'status', 'comment')

    def save_article(self, validated_data, user_obj, status='CREATED'):

        save_data, is_success = Article.objects.get_or_create(header=validated_data.get('header'),
                                                              body=validated_data.get('body'),
                                                              created_by=user_obj, status=status)
        if is_success and validated_data.get("comments", None):
            Comments.objects.create(article=save_data, text=validated_data.get('comments'), comment_by=user_obj)
        return save_data

    def update_article(self, instance, validated_data, user_obj):
        instance.header = validated_data.get('header')
        instance.body = validated_data.get('body')
        instance.status = validated_data.get('status')
        instance.save()
        if instance and validated_data.get("comments", None):
            Comments.objects.create(article=instance, text=validated_data.get('comments'), comment_by=user_obj)
        return instance


class CommentDetailsSerializer(serializers.ModelSerializer):
    replies = SerializerMethodField()
    user = SerializerMethodField()
    timestamp = SerializerMethodField()

    class Meta:
        model = Comments
        fields = (
            'id',
            'comment_by',
            'text',
            'timestamp'
        )

    @staticmethod
    def timestamp(obj):
        return obj.timesince()


class ArticleDataSerializer(serializers.ModelSerializer):
    comments = SerializerMethodField()
    createdBy = SerializerMethodField()

    class Meta:
        model = Article
        fields = ('header', 'body', 'createdAt', 'createdBy', 'status', 'comments')

    @staticmethod
    def get_comments(obj):
        return CommentDetailsSerializer(Comments.objects.filter_by_instance(obj),many=True).data

    @staticmethod
    def get_createdBy(obj):
        return {
            'email': obj.created_by.email,
            'id': obj.created_by.id,
            'isManager': obj.created_by.is_staff
        }
