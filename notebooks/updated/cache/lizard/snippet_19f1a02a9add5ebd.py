def pipeRecvGraph(self):
    try:
        while True:
            graph_rec = self.parent_pipe_recv_graph.recv()
            if graph_rec is not None:
                mestate.input_queue.put(graph_rec)
            time.sleep(0.1)
    except EOFError:
        pass