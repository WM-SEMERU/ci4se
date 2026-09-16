def graph_to_svg(graph):
    import tempfile
    import subprocess
    with tempfile.NamedTemporaryFile() as dot_file:
        nx.drawing.nx_agraph.write_dot(graph, dot_file.name)
        svg = subprocess.check_output(['dot', dot_file.name, '-Tsvg'])
    return svg