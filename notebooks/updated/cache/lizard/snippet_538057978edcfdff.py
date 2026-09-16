def get_toplevel_params(voevent):
    result = OrderedDict()
    w = deepcopy(voevent.What)
    lxml.objectify.deannotate(w)
    return _get_param_children_as_omdict(w)