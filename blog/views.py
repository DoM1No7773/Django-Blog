from django.shortcuts import render,get_object_or_404


from .models import Post

# Create your views here.
def index(request):
    post_list = Post.objects.order_by('created_at')[:5]
    context = {'post_list': post_list}
    return render(request, 'index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post})