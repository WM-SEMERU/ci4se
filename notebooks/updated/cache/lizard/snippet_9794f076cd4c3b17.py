def get_queryset(self):
    if 'sign' in self.request.query_params:
        try:
            filter_and_actions = unsign_filters_and_actions(self.request.
                query_params['sign'], '{}.{}'.format(self.queryset.model.
                _meta.app_label, self.queryset.model._meta.model_name))
        except signing.BadSignature:
            return super(SignedViewSetMixin, self).get_queryset()
        else:
            for filtered_action in filter_and_actions:
                try:
                    qs = self.queryset.filter(**filtered_action['filters'])
                except FieldError:
                    continue
                return qs
    return super(SignedViewSetMixin, self).get_queryset()