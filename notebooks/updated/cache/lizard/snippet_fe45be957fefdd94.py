def is_rfc2822(instance: str):
    if not isinstance(instance, str):
        return True
    return email.utils.parsedate(instance) is not None