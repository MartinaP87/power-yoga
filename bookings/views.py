from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import YogaType, YogaClass
from .forms import ReservationForm

import datetime


def mainp(request):
    return render(request, "index.html")


def class_type_list(request):
    yoga_types_list = YogaType.objects.filter(status=1)
    yoga_classes = YogaClass.objects.filter(status=1)
    context = {
        'yoga_types_list': yoga_types_list,
        'yoga_classes': yoga_classes,
        'reservation_form': ReservationForm()
    }
   
    print("ciao")
    return render(request, "classes.html", context)


def reserve(request):
    form = ReservationForm()
    if request.method == 'POST':
        if available_spaces > 0:
            messages.success(request, 'Your Reservation Was Successful!')
            reduce_availabele_spaces(class_id)
            return redirect('my_classes')
        else:
            messages.info(
                request, 'Unfortunately this class is fully booked.Why not picking another class?!')
            return redirect('classes')

# def add_reservation(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if available_spaces > 0:
#             if form.is_valid():
#                 form.save()
#                 return redirect('my_classes')
#         else:
#             messages.info(
#                 request, 'Unfortunately this class is fully booked.\
#                 Why not picking another class?!')
#             return redirect('classes')
#     form = ReservationForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'classes.html', context)

# class ClassDetail(View):

#     def get(self, request, id, *args, **kwargs):
#         queryset = YogaClass.objects.filter(status=1)
#         yoga_section = get_object_or_404(queryset, id=id)
#         reservations = yoga_section.reservations.filter(approved=True)
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
