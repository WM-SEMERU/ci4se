def need_record_permission(factory_name):

    def need_record_permission_builder(f):

        @wraps(f)
        def need_record_permission_decorator(self, record=None, *args, **kwargs
            ):
            permission_factory = getattr(self, factory_name) or getattr(
                current_records_rest, factory_name)
            request._methodview = self
            if permission_factory:
                verify_record_permission(permission_factory, record)
            return f(self, *args, record=record, **kwargs)
        return need_record_permission_decorator
    return need_record_permission_builder