def check_internal_ip(request):
    remote_addr = request.META['HTTP_X_FORWARDED_FOR'
        ] if 'HTTP_X_FORWARDED_FOR' in request.META else request.META.get(
        'REMOTE_ADDR', '')
    return remote_addr in settings.INTERNAL_IPS