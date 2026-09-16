def api_list(cls, api_key=djstripe_settings.STRIPE_SECRET_KEY, **kwargs):
    return cls.stripe_class.list(api_key=api_key, **kwargs).auto_paging_iter()