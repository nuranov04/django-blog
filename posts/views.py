from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import PostForm
from comments.models import Comment
from .models import Subscribe


def get_data(request):
    posts = Post.objects.all()
    if 'subscribe' in request.POST:
        id = request.POST.get('user_id')
        post_obj = Post.objects.get(id=id)
        try:
            subscribe = Subscribe.objects.get(user=request.user, post=post_obj)
            subscribe.delete()
        except:
            subscribe.objects.create(user=request.user, post=post_obj)
    return render(request, 'base.html', {'posts': posts})


def create(request):
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            post = Post()
            post.image = form.cleaned_data['image']
            post.user = request.user
            post.title = form.cleaned_data['title']
            post.description = form.cleaned_data['description']
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'create.html', {'form': form})


def detail_data(request, id):
    posts = Post.objects.get(id=id)
    if 'comment' in request.POST:
        id = request.POST.get('post_id')
        post = Post.objects.get(id=id)
        text = request.POST.get('comment_text')
        comment = Comment.objects.create(text=text, post=post, user=request.user)
    return render(request, 'detail.html', {"post": posts})
