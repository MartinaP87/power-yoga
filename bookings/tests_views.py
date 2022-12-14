from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .forms import ReservationForm
from .models import User, YogaType, YogaClass, Reservation
from datetime import date, timedelta


class TestViews(TestCase):

    def setUp(self):
        username = "Marla"
        password = "Django123"
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        login = self.client.login(username=username, password=password)
        self.assertTrue(login)

        self.yoga_type_test = YogaType.objects.create(
            title="test",
            slug="test",
            featured_image="",
            introduction="y",
            description="HelloDjango",
            status="1")

        self.yoga_class_1 = YogaClass.objects.create(
            yoga_type=self.yoga_type_test,
            day="2023-11-16",
            time="9:00 - 10:00",
            available_spaces="20",
            status="1")

        self.yoga_class_2 = YogaClass.objects.create(
            yoga_type=self.yoga_type_test,
            day="2022-11-16",
            time="9:00 - 10:00",
            available_spaces="20",
            status="1")

        self.yoga_class_3 = YogaClass.objects.create(
            yoga_type=self.yoga_type_test,
            day="2023-11-16",
            time="9:00 - 10:00",
            available_spaces="0",
            status="1")

        self.reservation_1 = Reservation.objects.create(
            yoga_class=self.yoga_class_1,
            member=self.user,
            approved="True"
        )

        self.reservation_2 = Reservation.objects.create(
            yoga_class=self.yoga_class_3,
            member=self.user,
            approved="False"
        )

        self.reservation_3 = Reservation.objects.create(
            yoga_class=self.yoga_class_3,
            member=self.user,
            approved="True"
        )

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_class_list(self):
        response = self.client.get('/classes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'classes.html')

    def test_reservations(self):
        response = self.client.get('/classes/reservations/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations.html')

    def test_book(self):
        response = self.client.get('/classes/book/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_class.html')

    # def check_double_booking(request, reservation):
    # current_user = request.user
    # yoga_class_users_reservations = Reservation.objects.filter(
    #     yoga_class_id=reservation.yoga_class_id)
    # yoga_class_user_reservations = \
    #     yoga_class_users_reservations.filter(member=current_user)
    # if yoga_class_user_reservations.count() > 1:
    #     messages.error(
    #             request, "You are already booked \
    #                 in for this class!")
    #     reservation.delete()
    # else:
    #     reserved_class_id = reservation.yoga_class_id
    #     updated_reservation = update_approval(
    #                     request, reservation.id)
    #     fully_booked(request, updated_reservation.id)

    def test_update_approval(self):
        # considering a reservation of a class with available spaces
        reservation_valid = self.reservation_1
        response_1 = self.client.post(
            f'/classes/update_approval/{reservation_valid.id}/')
        print("RESPONSE1: ", response_1)
        existing_reservation_1 = Reservation.objects.get(
            id=reservation_valid.id)
        self.assertEqual(existing_reservation_1.approved, True)
        # considering a reservation of a class with no available spaces
        reservation_not_valid = self.reservation_3
        response_2 = self.client.post(
            f'/classes/update_approval/{reservation_not_valid.id}/')
        print("RESPONSE2: ", response_2)
        existing_reservation_2 = Reservation.objects.get(
            id=reservation_not_valid.id)
        self.assertEqual(existing_reservation_2.approved, False)

    def test_fully_booked(self):
        reservation_valid = self.reservation_1
        reservation_not_valid = self.reservation_2
        response_1 = self.client.post(
            f'/classes/fully_booked/{reservation_valid.id}/')
        existing_reservation_1 = Reservation.objects.get(
            id=reservation_valid.id)
        self.assertTrue(existing_reservation_1.approved)
        response_2 = self.client.post(
            f'/classes/fully_booked/{reservation_not_valid.id}/')
    #             messages.error(
    #             request, 'Unfortunately the class is \
    # fully booked, choose another class!')
        existing_reservation_2 = Reservation.objects.filter(
            id=reservation_not_valid.id)
        self.assertEquals(len(existing_reservation_2), 0)

    def test_delete_reservation(self):
        reservation = self.reservation_1
        response = self.client.get(f'/classes/delete/{reservation.id}')
        self.assertRedirects(response, '/classes/reservations/')
        existing_reservation = Reservation.objects.filter(id=reservation.id)
        self.assertEquals(len(existing_reservation), 0)

    def test_reduce_available_spaces(self):
        initial_instance = YogaClass.objects.get(id=self.yoga_class_1.id)
        initial_spaces = int(initial_instance.available_spaces)
        response = self.client.post(
            f'/classes/reduce_available_spaces/{initial_instance.id}/')
        print("RESPONSE: ", response)
        updated_instance = YogaClass.objects.get(id=self.yoga_class_1.id)
        updated_spaces = int(updated_instance.available_spaces)
        print("UP", updated_spaces)
        self.assertEqual(updated_spaces, initial_spaces - 1)

    def test_increase_available_spaces(self):
        initial_instance = YogaClass.objects.get(id=self.yoga_class_1.id)
        initial_spaces = int(initial_instance.available_spaces)
        response = self.client.post(
            f'/classes/increase_available_spaces/{initial_instance.id}/')
        print("RESPONSE2: ", response)
        updated_instance = YogaClass.objects.get(id=self.yoga_class_1.id)
        updated_spaces = int(updated_instance.available_spaces)
        print("UP2", updated_spaces)
        self.assertEqual(updated_spaces, initial_spaces + 1)