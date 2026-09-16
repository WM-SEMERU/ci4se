def add_message(request, level, message, extra_tags='', fail_silently=False,
    *args, **kwargs):
    if hasattr(request, '_messages'):
        return request._messages.add(level, message, extra_tags, *args, **
            kwargs)
    if not fail_silently:
        raise MessageFailure(
            'You cannot add messages without installing django.contrib.messages.middleware.MessageMiddleware'
            )