def create(type_dict, *type_parameters):
    assert len(type_parameters) == 2
    name = type_parameters[0]
    alternatives = type_parameters[1]
    assert isinstance(name, Compatibility.stringy)
    assert isinstance(alternatives, (list, tuple))
    choice_types = []
    for c in alternatives:
        choice_types.append(TypeFactory.new(type_dict, *c))
    return TypeMetaclass(str(name), (ChoiceContainer,), {'CHOICES':
        choice_types})