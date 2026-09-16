def process_input_graph(func):

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        input_graph = args[0]
        if isinstance(input_graph, nx.DiGraph):
            return func(*args, **kwargs)
        else:
            nx_graph = dict_to_nx(args[0], oriented=True)
            args = [nx_graph] + list(args[1:])
            return func(*args, **kwargs)
    return wrapped_func