def validate_minimum(value, minimum, is_exclusive, **kwargs):
    if is_exclusive:
        comparison_text = 'greater than'
        compare_fn = operator.gt
    else:
        comparison_text = 'greater than or equal to'
        compare_fn = operator.ge
    if not compare_fn(value, minimum):
        raise ValidationError(MESSAGES['minimum']['invalid'].format(value,
            comparison_text, minimum))