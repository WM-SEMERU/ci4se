def get_uniform_comparator(comparator):
    if comparator in ['eq', 'equals', '==', 'is']:
        return 'equals'
    elif comparator in ['lt', 'less_than']:
        return 'less_than'
    elif comparator in ['le', 'less_than_or_equals']:
        return 'less_than_or_equals'
    elif comparator in ['gt', 'greater_than']:
        return 'greater_than'
    elif comparator in ['ge', 'greater_than_or_equals']:
        return 'greater_than_or_equals'
    elif comparator in ['ne', 'not_equals']:
        return 'not_equals'
    elif comparator in ['str_eq', 'string_equals']:
        return 'string_equals'
    elif comparator in ['len_eq', 'length_equals', 'count_eq']:
        return 'length_equals'
    elif comparator in ['len_gt', 'count_gt', 'length_greater_than',
        'count_greater_than']:
        return 'length_greater_than'
    elif comparator in ['len_ge', 'count_ge',
        'length_greater_than_or_equals', 'count_greater_than_or_equals']:
        return 'length_greater_than_or_equals'
    elif comparator in ['len_lt', 'count_lt', 'length_less_than',
        'count_less_than']:
        return 'length_less_than'
    elif comparator in ['len_le', 'count_le', 'length_less_than_or_equals',
        'count_less_than_or_equals']:
        return 'length_less_than_or_equals'
    else:
        return comparator