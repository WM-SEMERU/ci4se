def get_nx_graph(ea):
    nx_graph = networkx.DiGraph()
    func = idaapi.get_func(ea)
    flowchart = FlowChart(func)
    for block in flowchart:
        nx_graph.add_node(block.startEA)
        for pred in block.preds():
            nx_graph.add_edge(pred.startEA, block.startEA)
        for succ in block.succs():
            nx_graph.add_edge(block.startEA, succ.startEA)
    return nx_graph