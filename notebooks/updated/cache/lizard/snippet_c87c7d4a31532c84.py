def _get_dispatches_for_update(filter_kwargs):
    dispatches = Dispatch.objects.prefetch_related('message').filter(**
        filter_kwargs).select_for_update(**GET_DISPATCHES_ARGS[1]).order_by(
        '-message__time_created')
    try:
        dispatches = list(dispatches)
    except NotSupportedError:
        return None
    except DatabaseError:
        return []
    return dispatches