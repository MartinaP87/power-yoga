from .models import Reservation, YogaClass
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('yoga_class',)
