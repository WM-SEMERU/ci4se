def registration_settings(request):
    context = {}
    for setting in ('WAFER_SSO', 'WAFER_HIDE_LOGIN',
        'WAFER_REGISTRATION_OPEN', 'WAFER_REGISTRATION_MODE',
        'WAFER_TALKS_OPEN', 'WAFER_VIDEO_LICENSE'):
        context[setting] = getattr(settings, setting, None)
    return context