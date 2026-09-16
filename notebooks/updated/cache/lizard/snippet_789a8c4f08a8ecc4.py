def oembed(url, params=''):
    kwargs = dict(urlparse.parse_qsl(params))
    try:
        return mark_safe(get_oembed_data(url, **kwargs)['html'])
    except (KeyError, ProviderException):
        if settings.DEBUG:
            return 'No OEmbed data returned'
        return ''