from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from . import forms
import datetime

from .models import Post,Comment

# Create your views here.
def index(request):
    post_list = Post.objects.order_by('-created_at')
    context = {'post_list': post_list}
    return render(request, 'index.html', context)

def detail(request, post_id):
    if request.method == "POST":
        form = forms.CreateComment(request.POST)
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=request.POST.get('post'))
        comment.created_by = request.user
        comment.created_at = datetime.datetime.now()
        comment.save()
    else:
        form = forms.CreateComment

    post = get_object_or_404(Post, pk=post_id)

    try:
        comment_list = Comment.objects.filter(post=post)
        comment_list = comment_list.order_by('-created_at')
    except Comment.DoesNotExist:
        return render(request, 'detail.html', {'post': post})
    return render(request, 'detail.html', {'post': post,'comment_list':comment_list,'form':form})

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('blog:login')
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

@login_required(login_url="/login/")
def createPost(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            create_form = form.save(commit=False)
            create_form.created_at = datetime.datetime.now()
            create_form.created_by = request.user
            create_form.save()
            return redirect('blog:index')
    else:
        form = forms.CreatePost
    return render(request,'createPost.html',{'form':form})

@login_required(login_url="/login/")
def updatePost(request,post_id):

    post = get_object_or_404(Post,pk=post_id)
    form = forms.CreatePost()

    if request.method == "POST":
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post.created_at = datetime.datetime.now()
            post.created_by = request.user
            post.title = data['title']
            post.details = data['details']
            post.save()
            return redirect('/'+str(post_id)+'/')
    else:
        form.fields['title'].initial = post.title
        form.fields['details'].initial = post.details


    return render(request,'updatePost.html',{'form':form})

@login_required(login_url="/login/")
def deletePost(request,post_id):

    if request.method == "POST":
        post = get_object_or_404(Post,pk=post_id)
        post.delete()

    return redirect('blog:index')

@login_required(login_url="/login/")
def deleteComment(request,comment_id,post_id):

    if request.method == "POST":
        comment = get_object_or_404(Comment,pk=comment_id)
        comment.delete()

    return redirect('/'+str(post_id)+'/')
