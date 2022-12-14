from . import views
from django.urls import path

urlpatterns = [
    path('', views.class_list, name='classes'),
    path('book/', views.book, name='book'),
    path('reservations/', views.reservations, name='reservations'),
    path('delete/<reservation_id>', views.delete_reservation, name='delete'),
    path('reduce_available_spaces/<int:chosen_class_id>/', views.reduce_available_spaces, name='reduce'),
    path('increase_available_spaces/<int:chosen_class_id>/', views.increase_available_spaces, name='increase'),
    path('fully_booked/<int:reservation_id>/', views.fully_booked, name='fully_booked'),
    path('update_approval/<int:reservation_id>/', views.update_approval, name='update_approval'),

    # path('', views.ClassDetail.as_view(), name='classes'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
