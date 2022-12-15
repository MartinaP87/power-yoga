from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User, YogaType, YogaClass, Reservation
from django.contrib import messages
from .forms import ReservationForm
from datetime import date, timedelta


def home_page(request):
    todays_class = YogaClass.objects.filter(status=1, day=date.today())
    print("OGGI CLASSE", todays_class)
    context = {
        'todays_class': todays_class
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def class_list(request):
    yoga_types_list = YogaType.objects.filter(status=1)
    context = {
        'yoga_types_list': yoga_types_list
    }
    return render(request, "classes.html", context)


def reservations(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations.html', context)


def book(request):
    time_slots = ["9:00 - 10:00", "10:00 - 11:00",
                  "11:00 - 12:00", "14:00 - 15:00",
                  "15:00 - 16:00", "16:00 - 17:00",
                  "17:00 - 18:00", "20:00 - 21:00"]
    today = date.today()
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=13)
    week_days = [start + timedelta(days=i) for i in range((end-start).days+1)]
    yoga_classes = YogaClass.objects.filter(status=1)
    # delete non visible classes
    if yoga_classes:
        for yoga_class in yoga_classes:
            if yoga_class.day < start:
                yoga_class.delete()
    # allows classes to be accessable only if not in the past
    yoga_classes_available = []
    for yoga_class in yoga_classes:
        if yoga_class.day >= date.today():
            yoga_classes_available.append(yoga_class)
    # if method is post save form
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.member_id = request.user.id
            new_reservation = form.save()
            # valid_reservation(
            #     request, new_reservation, yoga_classes_available)
            if new_reservation.yoga_class in yoga_classes_available:
                if request.user.id == new_reservation.member.id:
                    current_user = request.user
                    yoga_class_user_reservations = Reservation.objects.filter(
                        yoga_class_id=new_reservation.yoga_class_id,
                        member=current_user)
                    if yoga_class_user_reservations.count() > 1:
                        messages.error(
                                request, "You are already booked \
                                    in for this class!")
                        new_reservation.delete()
                    else:
                        reserved_class_id = new_reservation.yoga_class_id
                # ---updated_reservation = update_approval(
                #     request, new_reservation)
                        queryset = YogaClass.objects.filter(status=1)
                        chosen_yoga_class = get_object_or_404(
                            queryset, id=reserved_class_id)
                        if chosen_yoga_class.available_spaces > 0:
                            new_reservation.approved
                            new_reservation.save()
                            reduce_available_spaces(
                                request, reserved_class_id)
                            return redirect('reservations')
                        else:
                            messages.error(
                                request, 'Unfortunately the class is \
    fully booked, choose another class!')
                            new_reservation.delete()
            else:
                messages.error(request, "This class is not longer available")
                new_reservation.delete()
    form = ReservationForm()
    context = {
        'time_slots': time_slots,
        'week_days': week_days,
        'yoga_classes': yoga_classes,
        'form': form
    }
    return render(request, 'book_class.html', context)


# def get_days(request):
#     today = date.today()
#     start = today - timedelta(days=today.weekday())
#     end = start + timedelta(days=13)
#     dates = [start + timedelta(days=i) for i in range((end-start).days+1)]
#     return (dates)


# def no_obsolete_classes(request):
#     week_days = get_days(request)
#     yoga_classes = YogaClass.objects.filter(status=1)
#     if yoga_classes:
#         for yoga_class in yoga_classes:
#             if yoga_class.day < week_days[0]:
#                 yoga_class.delete()
#                 # return redirect('book')
#     print("DA INIZIO SETTIMANA", yoga_classes)
#     return yoga_classes


# def yoga_classes_available(request):
#     yoga_classes = no_obsolete_classes(request)
#     yoga_classes_available = []
#     # allows classes to be accessable only if not in the past
#     for yoga_class in yoga_classes:
#         if yoga_class.day >= date.today():
#             yoga_classes_available.append(yoga_class)
#     return yoga_classes_available


# def valid_reservation(request, reservation, bookable_classes):
#     if reservation.yoga_class in bookable_classes:
#         check_double_booking(request, reservation.id)
#     else:
#         messages.error(request, "This class is not longer available")
#         new_reservation.delete()


# def check_double_booking(request, reservation_id):
#     reservation = get_object_or_404(Reservation, id=reservation_id)
#     current_user = request.user
#     yoga_class_user_reservations = Reservation.objects.filter(
#         yoga_class_id=reservation.yoga_class_id, member=current_user)
#     if yoga_class_user_reservations.count() > 1:
#         messages.error(
#                 request, "You are already booked \
#                     in for this class!")
#         reservation.delete()
#     else:
#         reserved_class_id = reservation.yoga_class_id
#         updated_reservation = update_approval(
#                         request, reservation.id)
#         fully_booked(request, updated_reservation.id)
#     return redirect('book')


# def update_approval(request, reservation_id):
#     reservation = get_object_or_404(Reservation, id=reservation_id)
#     reserved_class_id = reservation.yoga_class_id
#     queryset = YogaClass.objects.filter(status=1)
#     chosen_yoga_class = get_object_or_404(queryset, id=reserved_class_id)
#     if chosen_yoga_class.available_spaces > 0:
#         reservation.approved
#         reservation.save()
#     else:
#         reservation.approved = False
#         reservation.save()
#     return reservation
    # return reservation


# def fully_booked(request, reservation_id):
#     reservation = get_object_or_404(Reservation, id=reservation_id)
#     if reservation.approved:
#         reduce_available_spaces(
#             request, reservation.yoga_class_id)
#         return redirect('reservations')
#     else:
#         messages.error(
#             request, 'Unfortunately the class is \
# fully booked, choose another class!')
#         reservation.delete()
#         return redirect('book')


def reduce_available_spaces(request, chosen_class_id):
    queryset = YogaClass.objects.filter(status=1)
    chosen_yoga_class = get_object_or_404(queryset, id=chosen_class_id)
    spaces = int(chosen_yoga_class.available_spaces)
    updated_spaces = spaces - 1
    chosen_yoga_class.available_spaces = updated_spaces
    chosen_yoga_class.save()
    print("CLASSE ID E SPAZIO-", chosen_yoga_class.id,
          chosen_yoga_class.available_spaces)
    return redirect('reservations')


def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reserved_class_id = reservation.yoga_class_id
    reservation.delete()
    increase_available_spaces(request, reserved_class_id)
    return redirect('reservations')


def increase_available_spaces(request, chosen_class_id):
    queryset = YogaClass.objects.filter(status=1)
    chosen_yoga_class = get_object_or_404(queryset, id=chosen_class_id)
    spaces = int(chosen_yoga_class.available_spaces)
    updated_spaces = spaces + 1
    chosen_yoga_class.available_spaces = updated_spaces
    chosen_yoga_class.save()
    print("CLASSE ID E SPAZIO+", chosen_yoga_class.id,
          chosen_yoga_class.available_spaces)
    return redirect('reservations')
