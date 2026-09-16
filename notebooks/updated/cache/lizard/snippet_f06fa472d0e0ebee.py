def valid_service_context(service_context, when=0):
    eta = getattr(service_context, 'client_secret_expires_at', 0)
    now = when or utc_time_sans_frac()
    if eta != 0 and eta < now:
        return False
    return True