def moral_graph(model, format='raw', prog='dot', path=None, name=None):
    if not pydot_imported:
        raise ImportError(
            """PyDot must be installed to use the moral_graph function.
 PyDot is available from http://dkbza.org/pydot.html"""
            )
    model.moral_dot_object = pydot.Dot()
    for datum in model.observed_stochastics:
        model.moral_dot_object.add_node(pydot.Node(name=datum.__name__,
            style='filled'))
    for s in model.stochastics:
        model.moral_dot_object.add_node(pydot.Node(name=s.__name__))
    gone_already = set()
    for s in (model.stochastics | model.observed_stochastics):
        gone_already.add(s)
        for other_s in s.moral_neighbors:
            if not other_s in gone_already:
                model.moral_dot_object.add_edge(pydot.Edge(src=other_s.
                    __name__, dst=s.__name__, arrowhead='none'))
    ext = format
    if format == 'raw':
        ext = 'dot'
    if name is None:
        name = model.__name__
    name = name + '.' + ext
    if not path is None:
        model.moral_dot_object.write(path=os.path.join(path, name), format=
            format, prog=prog)
    else:
        model.moral_dot_object.write(path='./' + name, format=format, prog=prog
            )
    return model.moral_dot_object