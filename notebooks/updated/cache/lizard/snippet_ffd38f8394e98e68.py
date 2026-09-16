def is_subscribed(user, obj):
    if not user.is_authenticated():
        return False
    ctype = ContentType.objects.get_for_model(obj)
    try:
        Subscription.objects.get(user=user, content_type=ctype, object_id=
            obj.pk)
    except Subscription.DoesNotExist:
        return False
    return True