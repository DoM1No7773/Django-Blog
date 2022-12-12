from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required

from .models import Post,Comment

# Create your views here.
def index(request):
    post_list = Post.objects.order_by('created_at')[:5]
    context = {'post_list': post_list}
    return render(request, 'index.html', context)

@login_required(login_url="/login/")
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
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('blog:index')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def logoutUser(request):
    if request.method == "POST":
        logout(request)
        return redirect('blog:index')

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('blog:index')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


