def list_element_combinations_variadic(elements_specification):
    lists = [list(list_generated) for index, element_specification in
        enumerate(elements_specification) for list_generated in itertools.
        product(*elements_specification[:index + 1])]
    return lists