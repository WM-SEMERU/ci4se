def save_graph(graph_str, dest_file, fmt=None, image_ratio=None):
    g = pydot.graph_from_dot_data(graph_str)
    if fmt is None:
        fmt = os.path.splitext(dest_file)[1].lower().strip('.') or 'png'
    if hasattr(g, 'write_' + fmt):
        write_fn = getattr(g, 'write_' + fmt)
    else:
        raise Exception("Unsupported graph format: '%s'" % fmt)
    if image_ratio:
        g.set_ratio(str(image_ratio))
    write_fn(dest_file)
    return fmt