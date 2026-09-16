def dumps(*args, **kwargs):
    import json
    from django.conf import settings
    from argonauts.serializers import JSONArgonautsEncoder
    kwargs.setdefault('cls', JSONArgonautsEncoder)
    if settings.DEBUG:
        kwargs.setdefault('indent', 4)
        kwargs.setdefault('separators', (',', ': '))
    else:
        kwargs.setdefault('separators', (',', ':'))
    return json.dumps(*args, **kwargs)