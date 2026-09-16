def get_children(decider, root):
    collected = []

    def follow(elem):
        if elem in collected:
            return
        cls = elem.__class__
        if hasattr(cls, '_tx_attrs') and decider(elem):
            collected.append(elem)
        if hasattr(cls, '_tx_attrs'):
            for attr_name, attr in cls._tx_attrs.items():
                if attr.cont:
                    if attr.mult in (MULT_ONE, MULT_OPTIONAL):
                        new_elem = getattr(elem, attr_name)
                        if new_elem:
                            follow(new_elem)
                    else:
                        new_elem_list = getattr(elem, attr_name)
                        if new_elem_list:
                            for new_elem in new_elem_list:
                                follow(new_elem)
    follow(root)
    return collected