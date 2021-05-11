from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Content, Comment
from .forms import ContentForm, CommentForm
# Create your views here.
def home(request):
    posts = Content.objects.all()
    return render(request, 'sghouse/home.html', {'posts_list':posts})

def new(request):
    if request.method == 'POST':
        form = ContentForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = ContentForm()
    return render(request, 'sghouse/new.html',{'form':form})

def detail(request, index):
    post = get_object_or_404(Content, pk = index)
    comment_list = Comment.objects.filter(post=post)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.published_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('detail', index=index)
    else:
        comment_form = CommentForm()
    return render(request, 'sghouse/detail.html', {'post':post, 'comment_list':comment_list, 'comment_form':comment_form})

def edit(request, index):
    post = get_object_or_404(Content, pk = index)
    if request.method=='POST':
        form = ContentForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now
            post.save()
            return redirect('detail', index=post.pk)
    else:
        form = ContentForm(instance=post)
    return render(request, 'sghouse/edit.html',{'form':form})

def delete(request,pk):
    post = get_object_or_404(Content, pk=pk)
    post.delete()
    return redirect('home')

def delete_comment(request, index, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('detail', index=index)
