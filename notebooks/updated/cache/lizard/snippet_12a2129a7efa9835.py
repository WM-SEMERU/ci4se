def find_implementations(interface, recurse, abstract, result):
    for item in MetaComponent.implementations:
        if item['interface'] == interface and (abstract or not item['abstract']
            ):
            extend_unique(result, [item['class']])
    if recurse:
        subinterfaces = interface.__subclasses__()
        if subinterfaces:
            for i in subinterfaces:
                find_implementations(i, recurse, abstract, result)