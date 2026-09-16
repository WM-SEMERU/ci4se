def follow(user, obj, send_action=True, actor_only=True, flag='', **kwargs):
    check(obj)
    instance, created = apps.get_model('actstream', 'follow'
        ).objects.get_or_create(user=user, object_id=obj.pk, flag=flag,
        content_type=ContentType.objects.get_for_model(obj), actor_only=
        actor_only)
    if send_action and created:
        if not flag:
            action.send(user, verb=_('started following'), target=obj, **kwargs
                )
        else:
            action.send(user, verb=_('started %s' % flag), target=obj, **kwargs
                )
    return instance