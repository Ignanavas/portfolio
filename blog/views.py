import re
from django.shortcuts import render
from django.utils import timezone
from . models import Post
import requests


# Create your views here.
def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/index.html', {'post': posts})

def Postres(request):
        posts = Post.objects.filter(published_date_lte=timezone.now()).order_by('published_date')
        return render (request,'blog/index.html', {'post':posts} )

