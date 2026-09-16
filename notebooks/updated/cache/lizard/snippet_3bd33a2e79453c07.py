def do_graph(graph, prog=None, format='png', target=None, string=False,
    options=None, figsize=(12, 12), **kargs):
    from kamene.arch import NETWORKX
    if NETWORKX:
        import networkx as nx
    if NETWORKX and isinstance(graph, nx.Graph):
        nx.draw(graph, with_labels=True, edge_color='0.75', **kargs)
    else:
        if string:
            return graph
        if prog is None:
            prog = conf.prog.dot
        if not target or not format:
            format = 'png'
        format = '-T %s' % format
        p = subprocess.Popen('%s %s %s' % (prog, options or '', format or
            ''), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        w, r = p.stdin, p.stdout
        w.write(graph.encode('utf-8'))
        w.close()
        if target:
            with open(target, 'wb') as f:
                f.write(r.read())
        else:
            try:
                import matplotlib.image as mpimg
                import matplotlib.pyplot as plt
                figure = plt.figure(figsize=figsize)
                plt.axis('off')
                plt.imshow(mpimg.imread(r, format=format), **kargs)
                return figure
            except ImportError:
                warning(
                    'matplotlib.image required for interactive graph viewing. Use target option to write to a file'
                    )