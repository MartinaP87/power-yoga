from . import views
from django.urls import path

urlpatterns = [
    path('', views.class_type_list, name='classes'),
    path('<int:yoga_class_id>/', views.bookit, name='bookit')
    # path('', views.ClassDetail.as_view(), name='classes'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
