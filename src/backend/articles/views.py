from django.shortcuts import render
from .models import Article
from rest_framework import viewsets
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows articles to be viewed or edited.
	"""
	queryset = Article.objects.all().order_by('-created_at')
	serializer_class = ArticleSerializer