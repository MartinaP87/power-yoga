from django.shortcuts import render, get_object_or_404, redirect
from .models import YogaType, YogaClass, Reservation
from django.contrib import messages
from .forms import ReservationForm
import datetime


def home_page(request):
    return render(request, "index.html")


def class_list(request):
    yoga_types_list = YogaType.objects.filter(status=1)
    context = {
        'yoga_types_list': yoga_types_list,
    }
    return render(request, "classes.html", context)


def reservations(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations.html', context)


def book(request):
    yoga_classes = YogaClass.objects.filter(status=1)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            new_reservation = form.save()
            reserved_class_id = new_reservation.yoga_class_id
            update_approval(request, new_reservation)
            print(new_reservation.id)
            if new_reservation.approved:
                reduce_available_spaces(request, reserved_class_id)
                return redirect('reservations')
            else:
                messages.info(request, 'Unfortunately the class is fully booked, choose another class!')
                reservation = get_object_or_404(
                    Reservation, id=new_reservation.id)
                reservation.delete()
                return redirect('reservations')
    form = ReservationForm()
    context = {
        'yoga_classes': yoga_classes,
        'form': form
    }
    print(form)
    return render(request, 'book_class.html', context)


def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reserved_class_id = reservation.yoga_class_id
    reservation.delete()
    increase_available_spaces(request, reserved_class_id)
    return redirect('reservations')


def update_approval(request, reservation):
    reserved_class_id = reservation.yoga_class_id
    queryset = YogaClass.objects.filter(status=1)
    chosen_yoga_class = get_object_or_404(queryset, id=reserved_class_id)
    if chosen_yoga_class.available_spaces > 0:
        reservation.approved
        reservation.save()
    else:
        reservation.approved = False
        reservation.save()


def reduce_available_spaces(request, chosen_class_id):
    queryset = YogaClass.objects.filter(status=1)
    chosen_yoga_class = get_object_or_404(queryset, id=chosen_class_id)
    spaces = int(chosen_yoga_class.available_spaces)
    # if reservation.approved:
    updated_spaces = spaces - 1
    chosen_yoga_class.available_spaces = updated_spaces
    chosen_yoga_class.save()
    print("bo")
    print("YOGA", chosen_yoga_class.id, chosen_yoga_class.available_spaces)


def increase_available_spaces(request, chosen_class_id):
    queryset = YogaClass.objects.filter(status=1)
    chosen_yoga_class = get_object_or_404(queryset, id=chosen_class_id)
    spaces = int(chosen_yoga_class.available_spaces)
    updated_spaces = spaces + 1
    chosen_yoga_class.available_spaces = updated_spaces
    chosen_yoga_class.save()
    print("bodel")
    print("YOGA", chosen_yoga_class.id, chosen_yoga_class.available_spaces)

# def available_classes(request):
#     classes = get_object_or_404(YogaClass.objects.filter(status=1))
#     for single_class in classes:
#         if int(single_class.available_spaces) > 0:

# def update_yoga_class(request):
#     reservations = Reservation.objects.all()
#     for reservation in reservations:
#         yoga_class_id = reservation.yoga_class_id
#         queryset = YogaClass.objects.filter(status=1)
#         reserved_yoga_class = get_object_or_404(queryset, id=yoga_class_id)
#         spaces = int(reserved_yoga_class.available_spaces)
#         if reservation.approved:
#             updated_spaces = spaces - 1
#             reserved_yoga_class.available_spaces = updated_spaces
#             reserved_yoga_class.save()
#             print("bo")
#         print("YOGA", reserved_yoga_class.id, reserved_yoga_class.available_spaces)
# def book(request):
    # queryset = YogaClass.objects.filter(status=1)
    # yoga_class = get_object_or_404(queryset, id=yoga_class_id)
    # if request.method == 'POST':
    #     form = ReservationForm(request.POST)
    #         yoga_class=yoga_class,
    #         member=member
    #     )
    #     messages.success(request, "created appointment")
    #     return redirect('home')
    # return redirect('home')
    # queryset = YogaClass.objects.filter(status=1)
    # class_to_book = get_object_or_404(queryset, id=yoga_class_id)
    # reservations = class_to_book.reservations.filter(approved=True)
    # print(reservations)
    # available_spaces = class_to_book.available_spaces
    # reservation_form.fields["yoga_class"].queryset = YogaClass.objects.filter(
    #     id=yoga_class_id)
    # reservation_form = ReservationForm(data=request.POST)
    # if reservation_form.is_valid():
    #     print("form is valid")
    #     reservation_form.instance.member = request.user
    #     reservation = reservation_form.save(commit=False)
    #     reservation.class_to_book = class_to_book
    #     reservation.save()
    #     messages.success(request, 'Your Reservation Was Successful!')
            # availabele_spaces = int(availabele_spaces) - 1
            # return redirect('my_bookings')
    #     return redirect('home')
    # else:
    #     messages.info(
    #         request, 'Unfortunately this class is fully booked.Why not picking another class?!')
    #     return redirect('classes')
    # else:
    #     messages.info(request, 'Unfortunately...')
    #     reservation_form = ReservationForm()
    #     return render(
    #         request,
    #         "classes.html",
    #     )


# def add_reservation(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if available_spaces > 0:
#             if form.is_valid():
#                 available_spaces = int(available_spaces) - 1
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
