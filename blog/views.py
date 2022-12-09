from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm

from .models import Post,Comment

# Create your views here.
def index(request):
    post_list = Post.objects.order_by('created_at')[:5]
    context = {'post_list': post_list}
    return render(request, 'index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    try:
        comment_list = Comment.objects.filter(post=post)
    except Comment.DoesNotExist:
        return render(request, 'detail.html', {'post': post})
    return render(request, 'detail.html', {'post': post,'comment_list':comment_list})

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})