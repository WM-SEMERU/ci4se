def award_points(target, key, reason='', source=None):
    point_value, points = get_points(key)
    if not ALLOW_NEGATIVE_TOTALS:
        total = points_awarded(target)
        if total + points < 0:
            reason = reason + '(floored from {0} to 0)'.format(points)
            points = -total
    apv = AwardedPointValue(points=points, value=point_value, reason=reason)
    if isinstance(target, get_user_model()):
        apv.target_user = target
        lookup_params = {'target_user': target}
    else:
        apv.target_object = target
        lookup_params = {'target_content_type': apv.target_content_type,
            'target_object_id': apv.target_object_id}
    if source is not None:
        if isinstance(source, get_user_model()):
            apv.source_user = source
        else:
            apv.source_object = source
    apv.save()
    if not TargetStat.update_points(points, lookup_params):
        try:
            sid = transaction.savepoint()
            TargetStat._default_manager.create(**dict(lookup_params, points
                =points))
            transaction.savepoint_commit(sid)
        except IntegrityError:
            transaction.savepoint_rollback(sid)
            TargetStat.update_points(points, lookup_params)
    signals.points_awarded.send(sender=target.__class__, target=target, key
        =key, points=points, source=source)
    new_points = points_awarded(target)
    old_points = new_points - points
    TargetStat.update_positions((old_points, new_points))
    return apv