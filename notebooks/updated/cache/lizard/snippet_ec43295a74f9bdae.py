def from_dict(input_dict):
    import copy
    input_dict = copy.deepcopy(input_dict)
    link_class = input_dict.pop('class')
    import GPy
    link_class = eval(link_class)
    return link_class._build_from_input_dict(link_class, input_dict)