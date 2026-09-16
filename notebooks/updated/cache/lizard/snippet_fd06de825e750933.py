def validate_maximum(value, maximum, is_exclusive, **kwargs):
    if is_exclusive:
        comparison_text = 'less than'
        compare_fn = operator.lt
    else:
        comparison_text = 'less than or equal to'
        compare_fn = operator.le
    if not compare_fn(value, maximum):
        raise ValidationError(MESSAGES['maximum']['invalid'].format(value,
            comparison_text, maximum))