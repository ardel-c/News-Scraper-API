import json

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import News
from .serializers import NewsSerializer
from .scraper import create_news

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        
        if keyword is not None:
            create_news(keyword)
        queryset = News.objects.all()
        return queryset
