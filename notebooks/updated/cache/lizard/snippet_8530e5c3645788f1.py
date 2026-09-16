def remove_hooks(target, **hooks):
    for name, hook in hooks.items():
        hooked = getattr(target, name)
        if hook in hooked.pending:
            try:
                hooked.pending.remove(hook)
            except ValueError as e:
                raise ValueError('%s is not hooked by %s' % (target, hook)
                    ) from e
        if not hooked.pending:
            setattr(target, name, hooked.func)