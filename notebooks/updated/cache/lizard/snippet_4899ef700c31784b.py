def persistant_info(request, message, extra_tags='', fail_silently=False, *
    args, **kwargs):
    add_message(request, INFO_PERSISTENT, message, *args, extra_tags=
        extra_tags, fail_silently=fail_silently, **kwargs)