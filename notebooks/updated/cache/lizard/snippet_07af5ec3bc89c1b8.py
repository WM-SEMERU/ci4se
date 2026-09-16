def neighbours_pattern(element):
    if not element.parent:
        return []
    parent = element.parent
    neighbours = filter(lambda x: x.isTag() and not x.isEndTag() or x.
        getContent().strip() or x is element, parent.childs)
    if len(neighbours) <= 1:
        return []
    output = []
    element_index = neighbours.index(element)
    if element_index >= 1:
        output.append(_neighbour_to_path_call('left', neighbours[
            element_index - 1], element))
    if element_index + 1 < len(neighbours):
        output.append(_neighbour_to_path_call('right', neighbours[
            element_index + 1], element))
    return output