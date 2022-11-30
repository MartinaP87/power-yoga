from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import YogaType, YogaClass
from .forms import ReservationForm
import datetime
from django.shortcuts import render, redirect, get_object_or_404


def mainp(request):
    return render(request, "index.html")


def class_type_list(request):
    yoga_types_list = YogaType.objects.filter(status=1)
    yoga_classes = YogaClass.objects.filter(status=1)
    context = {
        'yoga_types_list': yoga_types_list,
        'yoga_classes': yoga_classes
    }
    return render(request, "classes.html", context)


# class ClassDetail(View):

#     def get(self, request, yoga_type, *args, **kwargs):
#         queryset = YogaClass.objects.filter(status=1)
#         yoga_section = get_object_or_404(queryset, yoga_type=yoga_type)
#         reservations = yoga_class.reservations.filter(approved=True)
#         return render(
#             request,
#             "classes.html",
#             {
#                 "yoga_section": yoga_section,
#                 "reservations": reservations,
#                 "reservation_form": ReservationForm()
#             },
#         )

#     def post(self, request, slug, *args, **kwargs):

#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by(
# "-created_on")
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             comment_form.instance.email = request.user.email
#             comment_form.instance.name = request.user.username
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.save()
#         else:
#             comment_form = CommentForm()

#         return render(
#             request,
#             "post_detail.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": True,
#                 "comment_form": comment_form,
#                 "liked": liked
#             },
#         )
#   class PostDetail(View):
#     def get(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by(
# "-created_on")
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True
#         return render(
#             request,
#             "post_detail.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": False,
#                 "liked": liked,
#                 "comment_form": CommentForm()
#             },
#         )
#     def post(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by(
# "-created_on")
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             comment_form.instance.email = request.user.email
#             comment_form.instance.name = request.user.username
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.save()
#         else:
#             comment_form = CommentForm()
#         return render(
#             request,
#             "post_detail.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": True,
#                 "comment_form": comment_form,
#                 "liked": liked
#             },
#         )

