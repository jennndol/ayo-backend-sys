from .models import Article
from rest_framework import serializers

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Article
		fields = ('title','slug','content','status','created_by','created_at','updated_at')