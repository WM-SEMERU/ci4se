def BuildAdGroupCriterionOperations(adgroup_operations, number_of_keywords=1):
    criterion_operations = [{'xsi_type': 'AdGroupCriterionOperation',
        'operand': {'xsi_type': 'BiddableAdGroupCriterion', 'adGroupId':
        adgroup_operation['operand']['id'], 'criterion': {'xsi_type':
        'Keyword', 'text': 'mars%s%s' % (i, '!!!' if i % 2 == 0 else ''),
        'matchType': 'BROAD'}}, 'operator': 'ADD'} for adgroup_operation in
        adgroup_operations for i in range(number_of_keywords)]
    return criterion_operations