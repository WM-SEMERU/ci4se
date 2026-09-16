def get_grouped_params(voevent):
    groups_omd = OMDict()
    w = deepcopy(voevent.What)
    lxml.objectify.deannotate(w)
    if w.find('Group') is not None:
        for grp in w.Group:
            groups_omd.add(grp.attrib.get('name'),
                _get_param_children_as_omdict(grp))
    return groups_omd