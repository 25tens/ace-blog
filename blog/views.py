from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    post_list= Post.objects.all()
    return render(request,'blog/post_list.html',{'post_list':post_list,})