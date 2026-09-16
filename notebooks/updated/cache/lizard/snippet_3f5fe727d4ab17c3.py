def select_edges_by_attribute(docgraph, attribute=None, value=None, data=False
    ):
    if attribute:
        attrib_key_eval = "'{}' in edge_attribs".format(attribute)
        if value is not None:
            if isinstance(value, basestring):
                attrib_val_eval = "edge_attribs['{0}'] == '{1}'".format(
                    attribute, value)
                return select_edges(docgraph, data=data, conditions=[
                    attrib_key_eval, attrib_val_eval])
            else:
                attrib_val_evals = ["edge_attribs['{0}'] == '{1}'".format(
                    attribute, v) for v in value]
                results = [select_edges(docgraph, data=data, conditions=[
                    attrib_key_eval, val_eval]) for val_eval in
                    attrib_val_evals]
                return itertools.chain(*results)
        else:
            return select_edges(docgraph, data=data, conditions=[
                attrib_key_eval])
    else:
        return docgraph.edges_iter(data=data)