def can_manage(user, semester=None, pool=None, any_pool=False):
    if semester and user in semester.workshift_managers.all():
        return True
    if Manager and Manager.objects.filter(incumbent__user=user,
        workshift_manager=True).count() > 0:
        return True
    if pool and pool.managers.filter(incumbent__user=user).count() > 0:
        return True
    if any_pool and WorkshiftPool.objects.filter(managers__incumbent__user=user
        ):
        return True
    return user.is_superuser or user.is_staff