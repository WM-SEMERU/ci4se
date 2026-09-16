def index_view(request, auth_form=None, force_login=False, added_context=None):
    if request.user.is_authenticated and not force_login:
        return dashboard_view(request)
    else:
        auth_form = auth_form or AuthenticateForm()
        request.session.set_test_cookie()
        fcps_emerg = get_fcps_emerg(request)
        try:
            login_warning = settings.LOGIN_WARNING
        except AttributeError:
            login_warning = None
        if fcps_emerg and not login_warning:
            login_warning = fcps_emerg
        ap_week = get_ap_week_warning(request)
        if ap_week and not login_warning:
            login_warning = ap_week
        events = Event.objects.filter(time__gte=datetime.now(), time__lte=
            datetime.now().date() + relativedelta(weeks=1), public=True
            ).this_year()
        sports_events = events.filter(approved=True, category='sports'
            ).order_by('time')[:3]
        school_events = events.filter(approved=True, category='school'
            ).order_by('time')[:3]
        data = {'auth_form': auth_form, 'request': request, 'git_info':
            settings.GIT, 'bg_pattern': get_bg_pattern(), 'theme':
            get_login_theme(), 'login_warning': login_warning,
            'senior_graduation': settings.SENIOR_GRADUATION,
            'senior_graduation_year': settings.SENIOR_GRADUATION_YEAR,
            'sports_events': sports_events, 'school_events': school_events}
        schedule = schedule_context(request)
        data.update(schedule)
        if added_context is not None:
            data.update(added_context)
        return render(request, 'auth/login.html', data)