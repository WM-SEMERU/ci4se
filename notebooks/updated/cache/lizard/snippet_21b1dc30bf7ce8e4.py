def get_now():
    if not get_current_request:
        return datetime.datetime.now()
    request = get_current_request()
    if request:
        openinghours_now = request.GET.get('openinghours-now')
        if openinghours_now:
            return datetime.datetime.strptime(openinghours_now, '%Y%m%d%H%M%S')
    return datetime.datetime.now()