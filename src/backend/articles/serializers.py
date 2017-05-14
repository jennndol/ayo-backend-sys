from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new Article instance, given the validated data
        :param validated_data: title, content
        :return: Article instance
        """
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Article instance, given the validated data.
        :param instance: article
        :param validated_data: title, content
        :return: instance
        """
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.title)
        instance.save()
        return instance
