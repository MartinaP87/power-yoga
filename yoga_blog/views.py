from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .forms import CommentForm


def post_list(request):
    post_list = Post.objects.filter(status=1).order_by("-created_on")
    context = {
        'post_list': post_list
    }
    return render(request, "yoga_blog/blog.html", context)


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    commented = False
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            commented = True
            messages.success(
                request, 'You successfully left a comment.<br>\
                Your comment is waiting for approval.')
        else:
            comment_form = CommentForm()
    context = {
                "post": post,
                "comments": comments,
                "commented": commented,
                "liked": liked,
                "comment_form": comment_form,
            }
    return render(request, "yoga_blog/post_detail.html", context)





def post_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('post_detail', slug)
