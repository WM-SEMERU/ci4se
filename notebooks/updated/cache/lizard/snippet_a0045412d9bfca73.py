def toposort_rules(rules):
    graph = {}
    class_dict = {}
    for rule in rules:
        if rule.__class__ in class_dict:
            raise ValueError('Duplicate class rules are not allowed: %s' %
                rule.__class__)
        class_dict[rule.__class__] = rule
    for rule in rules:
        if not is_iterable(rule.dependency) and rule.dependency:
            rule_dependencies = [rule.dependency]
        else:
            rule_dependencies = rule.dependency
        dependencies = set()
        if rule_dependencies:
            for dependency in rule_dependencies:
                if inspect.isclass(dependency):
                    dependency = class_dict.get(dependency)
                if dependency:
                    dependencies.add(dependency)
        graph[rule] = dependencies
    return toposort(graph)