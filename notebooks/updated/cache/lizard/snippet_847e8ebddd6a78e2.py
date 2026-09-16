def display_graph(graphdef):
    mestate.console.write('Expression: %s\n' % ' '.join(graphdef.expression
        .split()))
    child = multiprocessing.Process(target=graph_process, args=[graphdef.
        expression.split()])
    child.start()