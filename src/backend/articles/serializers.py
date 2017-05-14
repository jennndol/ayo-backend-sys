from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new Article instance, given the validated data
        :param validated_data: 
        :return: Article instance
        """
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        :param instance: 
        :param validated_data: 
        :return: instance
        """
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.title)
        instance.save()
        return instance
