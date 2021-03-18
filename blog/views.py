from django.shortcuts import render
from .models import Post
from django.utils import timezone
#  . はカレントディレクトリorカレントアプリケーション
# views.py ,models.py が同じディレクトリにあるから可能

def post_list(request):
  posts =Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'blog/post_list.html',{'posts':posts})
  