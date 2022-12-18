from .models import Reservation, Notes
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('yoga_class',)


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('reservation', 'annotation',)
