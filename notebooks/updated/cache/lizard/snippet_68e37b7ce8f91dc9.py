def _create_fulltext_query(self):
    filter_by = []
    if 'q' in request.args:
        columns = flat_model(model_tree(self.__class__.__name__, self.
            model_cls))
        for q in request.args.getlist('q'):
            filter_by += ['{col}::like::%{q}%'.format(col=col, q=q) for col in
                columns]
    return filter_by