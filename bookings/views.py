from django.shortcuts import render, get_object_or_404, redirect
from .models import User, YogaType, YogaClass, Reservation
from django.contrib import messages
from .forms import ReservationForm
from datetime import date, timedelta


def home_page(request):
    return render(request, "index.html")


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
    week_days = get_days(request)
    yoga_classes = weekly_classes(request)
    yoga_classes_available_now = []
    for yoga_class in yoga_classes:
        if yoga_class.day >= date.today():
            yoga_classes_available_now.append(yoga_class)
    print("POSSIBILI CLASSI", yoga_classes_available_now)
  
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            new_reservation = form.save()
            if new_reservation.yoga_class in yoga_classes_available_now:
                if request.user.id == new_reservation.member.id:
                    reserved_class_id = new_reservation.yoga_class_id
                    update_approval(request, new_reservation)
                    print(new_reservation.id)
                    print("MEMBRO NEWRES", new_reservation.member)
                    if new_reservation.approved:
                        reduce_available_spaces(request, reserved_class_id)
                        return redirect('reservations')
                    else:
                        print("fullybooked")
                        reservation = get_object_or_404(
                            Reservation, id=new_reservation.id)
                        messages.error(
                            request, 'Unfortunately the class is fully booked, choose another class!')
                        new_reservation.delete()
                else:
                    messages.warning(
                        request, "To book a class with a different account login with its details")
                    new_reservation.delete()
            else:
                messages.error(request, "This class is not longer available")
                new_reservation.delete()
    form = ReservationForm()
    context = {
        'week_days': week_days,
        'yoga_classes': yoga_classes,
        'form': form
    }
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
    updated_spaces = spaces - 1
    chosen_yoga_class.available_spaces = updated_spaces
    chosen_yoga_class.save()
    print("CLASSE ID E SPAZIO-", chosen_yoga_class.id, chosen_yoga_class.available_spaces)


def increase_available_spaces(request, chosen_class_id):
    queryset = YogaClass.objects.filter(status=1)
    chosen_yoga_class = get_object_or_404(queryset, id=chosen_class_id)
    spaces = int(chosen_yoga_class.available_spaces)
    updated_spaces = spaces + 1
    chosen_yoga_class.available_spaces = updated_spaces
    chosen_yoga_class.save()
    print("CLASSE ID E SPAZIO+", chosen_yoga_class.id, chosen_yoga_class.available_spaces)


def get_days(request):
    today = date.today()
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=20)
    dates = [start + timedelta(days=i) for i in range((end-start).days+1)]
    return (dates)


def weekly_classes(request):
    week_days = get_days(request)
    yoga_classes = YogaClass.objects.filter(status=1)
    if yoga_classes:
        for yoga_class in yoga_classes:
            if yoga_class.day < week_days[0]:
                yoga_class.delete()
    print("DA INIZIO SETTIMANA", yoga_classes)
    return yoga_classes
