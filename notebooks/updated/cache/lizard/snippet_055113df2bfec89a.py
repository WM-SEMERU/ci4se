def get_ip(request):
    if config.BEHIND_REVERSE_PROXY:
        ip_address = request.META.get(config.REVERSE_PROXY_HEADER, '')
        ip_address = ip_address.split(',', 1)[0].strip()
        if ip_address == '':
            ip_address = get_ip_address_from_request(request)
    else:
        ip_address = get_ip_address_from_request(request)
    return ip_address