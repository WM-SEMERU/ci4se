def _build_function_dependency_graphs(self):
    self._function_data_dependencies = defaultdict(networkx.DiGraph)
    block_addr_to_func = {}
    for _, func in self.kb.functions.items():
        for block in func.blocks:
            block_addr_to_func[block.addr] = func
    for src, dst, data in self.graph.edges(data=True):
        src_target_func = None
        if src.block_addr in block_addr_to_func:
            src_target_func = block_addr_to_func[src.block_addr]
            self._function_data_dependencies[src_target_func].add_edge(src,
                dst, **data)
        if dst.block_addr in block_addr_to_func:
            dst_target_func = block_addr_to_func[dst.block_addr]
            if not dst_target_func is src_target_func:
                self._function_data_dependencies[dst_target_func].add_edge(src,
                    dst, **data)