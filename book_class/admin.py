from django.contrib import admin
from .models import YogaClass, Reservation
from django_summernote.admin import SummernoteModelAdmin


@admin.register(YogaClass)
class YogaClassAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('yoga_type',)}
    list_filter = ('status', 'yoga_type')
    list_display = ('yoga_type', 'status')
    search_fields = ['yoga_type', 'description']
    summernote_fields = ('description')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_filter = ('yoga_class', 'approved',)
    list_display = ('yoga_class', 'day', 'time', 'name', 'surname', 'approved')
    search_fields = [
        'name', 'surname', 'yoga_class']
    actions = ['approve_class']

    def approve_class(self, request, queryset):
        queryset.update(approved=True)
