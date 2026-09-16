def register_all(module, exclude=[], AdminClass=admin.ModelAdmin):
    member_names = dir(module)
    for member_name in member_names:
        obj = getattr(module, member_name, None)
        if isinstance(obj, ModelBase
            ) and obj not in exclude and not obj._meta.abstract:
            try:
                if hasattr(obj, 'localized_fields'):
                    admin.site.register(obj, L10n(obj, AdminClass))
                else:
                    admin.site.register(obj, AdminClass)
            except AlreadyRegistered:
                pass