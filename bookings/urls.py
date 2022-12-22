from . import views
from django.urls import path

urlpatterns = [
    path('', views.class_list, name='classes'),
    path('book/', views.book, name='book'),
    path('reservations/', views.reservations, name='reservations'),
    path('delete/<reservation_id>', views.delete_reservation, name='delete'),
    path('delete/note/<note_id>', views.delete_note, name='delete_note'),
    path('edit/note/<note_id>', views.edit_note, name='edit_note'),
    # path('reduce_available_spaces/<int:chosen_class_id>/', views.reduce_available_spaces, name='reduce'),
    # path('increase_available_spaces/<int:chosen_class_id>/', views.increase_available_spaces, name='increase'),
    # path('fully_booked/<int:reservation_id>/', views.fully_booked, name='fully_booked'),
    # path('update_approval/<int:reservation_id>/', views.update_approval, name='update_approval'),
    # path('check_double_booking/<int:reservation_id>/', views.check_double_booking, name='check_double_booking'),
]