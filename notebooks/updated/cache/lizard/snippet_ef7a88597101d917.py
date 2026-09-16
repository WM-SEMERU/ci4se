def possible_parameter(nb, jsonable_parameter=True, end_cell_index=None):
    jh = _JupyterNotebookHelper(nb, jsonable_parameter, end_cell_index)
    if jsonable_parameter is True:
        PossibleParameter = collections.namedtuple('PossibleParameter', [
            'name', 'value', 'cell_index'])
    else:
        PossibleParameter = collections.namedtuple('PossibleParameter', [
            'name', 'cell_index'])
    res = []
    for name, cell_index in jh.param_cell_index.items():
        if jsonable_parameter is True:
            res.append(PossibleParameter(name=name, value=jh.param_value[
                name], cell_index=cell_index))
        else:
            res.append(PossibleParameter(name=name, cell_index=cell_index))
    return sorted(res, key=lambda x: x.name)