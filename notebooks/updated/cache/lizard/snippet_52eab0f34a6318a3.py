def persist_booking(booking, user):
    if booking is not None:
        existing_bookings = Booking.objects.filter(user=user,
            booking_status__slug='inprogress').exclude(pk=booking.pk)
        existing_bookings.delete()
        booking.session = None
        booking.user = user
        booking.save()