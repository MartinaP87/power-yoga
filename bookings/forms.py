from .models import Reservation, Notes
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('yoga_class',)
        labels = {
            'yoga_class': ('Yoga Class'),
        }


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('reservation', 'annotation',)
        labels = {
            'annotation': ('Note'),
        }
    
    # def __init__(self, *args, **kwargs):
    #     super(NotesForm, self).__init__(*args, **kwargs)
    #     self.fields['reservation'].queryset = Reservation.objects.filter(
    #         member=request.user)
