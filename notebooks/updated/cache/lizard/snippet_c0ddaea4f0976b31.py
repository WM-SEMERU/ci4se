def _parse_structure(element, reference):
    data = {'reference': reference}
    content_type = reference[0]
    if content_type in ('sequence', 'choice'):
        children = reference[1]
        ordered_children = []
        structure = {}
        structure_by_longname = {}
        repetitions = {}
        counters = collections.defaultdict(int)
        for c in children:
            child_name, child_ref, cardinality, cls = c
            k = (child_name if child_name not in structure else '{0}_{1}'.
                format(child_name, counters[child_name]))
            structure[k] = {'ref': child_ref, 'name': k, 'cls': element.
                child_classes[cls]}
            try:
                structure_by_longname[child_ref[3]] = structure[k]
            except IndexError:
                pass
            counters[child_name] += 1
            repetitions[k] = cardinality
            ordered_children.append(k)
        data['repetitions'] = repetitions
        data['ordered_children'] = ordered_children
        data['structure_by_name'] = structure
        data['structure_by_longname'] = structure_by_longname
    if len(reference) > 5:
        datatype, long_name, table, max_length = reference[2:]
        data['datatype'] = datatype
        data['table'] = table
        data['long_name'] = long_name
    return data