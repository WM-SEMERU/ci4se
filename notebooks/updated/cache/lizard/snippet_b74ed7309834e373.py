def get_fields(self):
    fields = super(BaseHookSerializer, self).get_fields()
    fields['event_types'] = serializers.MultipleChoiceField(choices=loggers
        .get_valid_events(), required=False)
    fields['event_groups'] = serializers.MultipleChoiceField(choices=
        loggers.get_event_groups_keys(), required=False)
    return fields