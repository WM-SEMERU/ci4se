def stringify(pkgs):
    try:
        for key in pkgs:
            pkgs[key] = ','.join(pkgs[key])
    except AttributeError as exc:
        log.exception(exc)