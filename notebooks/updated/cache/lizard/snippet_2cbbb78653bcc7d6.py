def _neighbour_to_path_call(neig_type, neighbour, element):
    params = [None, None, neighbour.getContent().strip()]
    if neighbour.isTag():
        params = [neighbour.getTagName(), _params_or_none(neighbour.params),
            neighbour.getContent().strip()]
    return PathCall(neig_type + '_neighbour_tag', 0, NeighCall(element.
        getTagName(), _params_or_none(element.params), params))