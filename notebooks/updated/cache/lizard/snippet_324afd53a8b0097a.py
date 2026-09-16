def check(self, dsm, independence_factor=5, **kwargs):
    least_common_mechanism = False
    message = ''
    data = dsm.data
    categories = dsm.categories
    dsm_size = dsm.size[0]
    if not categories:
        categories = ['appmodule'] * dsm_size
    dependent_module_number = []
    for j in range(0, dsm_size):
        dependent_module_number.append(0)
        for i in range(0, dsm_size):
            if categories[i] != 'framework' and categories[j
                ] != 'framework' and data[i][j] > 0:
                dependent_module_number[j] += 1
    for index, item in enumerate(dsm.categories):
        if item == 'broker' or item == 'applib':
            dependent_module_number[index] = 0
    if max(dependent_module_number) <= dsm_size / independence_factor:
        least_common_mechanism = True
    else:
        maximum = max(dependent_module_number)
        message = (
            'Dependencies to %s (%s) > matrix size (%s) / independence factor (%s) = %s'
             % (dsm.entities[dependent_module_number.index(maximum)],
            maximum, dsm_size, independence_factor, dsm_size /
            independence_factor))
    return least_common_mechanism, message