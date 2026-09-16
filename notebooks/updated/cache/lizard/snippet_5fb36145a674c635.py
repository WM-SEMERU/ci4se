def absence_count(request):
    if (request.user and request.user.is_authenticated and request.user.
        is_student):
        absence_info = request.user.absence_info()
        num_absences = absence_info.count()
        show_notif = False
        if num_absences > 0:
            notif_seen = request.session.get('eighth_absence_notif_seen', False
                )
            if not notif_seen:
                for signup in absence_info:
                    if signup.in_clear_absence_period():
                        show_notif = True
            if show_notif:
                request.session['eighth_absence_notif_seen'] = True
        return {'eighth_absence_count': num_absences,
            'eighth_absence_notif': show_notif}
    return {}