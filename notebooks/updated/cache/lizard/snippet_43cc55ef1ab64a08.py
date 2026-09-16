def get_true_false_both(query_params, field_name, default):
    valid = 'true', 'false', 'both'
    value = query_params.get(field_name, default).lower()
    if value in valid:
        return value
    v = ', '.join(sorted(valid))
    raise serializers.ValidationError({field_name: ['Must be one of [%s]' % v]}
        )