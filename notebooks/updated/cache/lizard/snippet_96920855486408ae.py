def _get_instance(user):
    inst = None
    f = Usuario.objects.filter(user=user)
    if f.exists():
        inst = f[0]
        for sub_u in Usuario.__subclasses__():
            if hasattr(inst, sub_u.__name__.lower()):
                inst = getattr(inst, sub_u.__name__.lower())
                break
    return inst