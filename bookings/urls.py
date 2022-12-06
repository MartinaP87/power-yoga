from . import views
from django.urls import path

urlpatterns = [
    path('', views.class_list, name='classes'),
    path('book/', views.book, name='book'),
    path('reservations/', views.reservations, name='reservations')
    # path('', views.ClassDetail.as_view(), name='classes'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
