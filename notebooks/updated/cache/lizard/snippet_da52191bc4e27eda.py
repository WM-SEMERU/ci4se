def persistant_error(request, message, extra_tags='', fail_silently=False,
    *args, **kwargs):
    add_message(request, ERROR_PERSISTENT, message, *args, extra_tags=
        extra_tags, fail_silently=fail_silently, **kwargs)