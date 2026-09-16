def condition_expression_to_expected(condition_expression,
    expression_attribute_names, expression_attribute_values):
    expected = {}
    if condition_expression and 'OR' not in condition_expression:
        reverse_re = re.compile('^NOT\\s*\\((.*)\\)$')
        reverse_m = reverse_re.match(condition_expression.strip())
        reverse = False
        if reverse_m:
            reverse = True
            condition_expression = reverse_m.group(1)
        cond_items = [c.strip() for c in condition_expression.split('AND')]
        if cond_items:
            exists_re = re.compile('^attribute_exists\\s*\\((.*)\\)$')
            not_exists_re = re.compile('^attribute_not_exists\\s*\\((.*)\\)$')
            equals_re = re.compile('^(#?\\w+)\\s*=\\s*(\\:?\\w+)')
        for cond in cond_items:
            exists_m = exists_re.match(cond)
            not_exists_m = not_exists_re.match(cond)
            equals_m = equals_re.match(cond)
            if exists_m:
                attribute_name = expression_attribute_names_lookup(exists_m
                    .group(1), expression_attribute_names)
                expected[attribute_name] = {'Exists': True if not reverse else
                    False}
            elif not_exists_m:
                attribute_name = expression_attribute_names_lookup(not_exists_m
                    .group(1), expression_attribute_names)
                expected[attribute_name] = {'Exists': False if not reverse else
                    True}
            elif equals_m:
                attribute_name = expression_attribute_names_lookup(equals_m
                    .group(1), expression_attribute_names)
                attribute_value = expression_attribute_values_lookup(equals_m
                    .group(2), expression_attribute_values)
                expected[attribute_name] = {'AttributeValueList': [
                    attribute_value], 'ComparisonOperator': 'EQ' if not
                    reverse else 'NEQ'}
    return expected