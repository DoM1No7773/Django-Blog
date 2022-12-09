from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.
def index(request):
    post_list = Post.objects.order_by('created_at')[:5]
    output = ', '.join([q.title for q in post_list])
    return HttpResponse(output)

def detail(request, post_id):
    return HttpResponse("post_id : %s." % post_id)