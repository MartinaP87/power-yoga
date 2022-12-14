from django.test import TestCase
from .forms import ReservationForm


class TestReservationForm(TestCase):

    def test_yoga_class_is_required(self):
        form = ReservationForm({"yoga_class": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("yoga_class", form.errors.keys())
        self.assertEqual(
            form.errors["yoga_class"][0], "This field is required.")

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReservationForm()
        self.assertEqual(form.Meta.fields, ('yoga_class',))
