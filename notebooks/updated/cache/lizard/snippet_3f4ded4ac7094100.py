def lockout_response(request):
    if config.LOCKOUT_TEMPLATE:
        context = {'cooloff_time_seconds': config.COOLOFF_TIME,
            'cooloff_time_minutes': config.COOLOFF_TIME / 60,
            'failure_limit': config.FAILURE_LIMIT}
        return render(request, config.LOCKOUT_TEMPLATE, context)
    if config.LOCKOUT_URL:
        return HttpResponseRedirect(config.LOCKOUT_URL)
    if config.COOLOFF_TIME:
        return HttpResponse(
            'Account locked: too many login attempts.  Please try again later.'
            )
    else:
        return HttpResponse(
            'Account locked: too many login attempts.  Contact an admin to unlock your account.'
            )