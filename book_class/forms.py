from .models import Reservation
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'surname', 'yoga_class', 'day', 'time')
