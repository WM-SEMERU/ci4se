def maas_archive(begin, end):
    base_url = 'http://marsweather.ingenology.com/v1/archive/?'
    try:
        vali_date(begin)
        vali_date(end)
        base_url += ('terrestrial_date_start=' + begin + '&' +
            'terrestrial_date_end=' + end)
    except:
        raise ValueError('Incorrect date format, should be YYYY-MM-DD')
    return dispatch_http_get(base_url)