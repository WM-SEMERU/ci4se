def _create_graph(self, return_target_sources=None):
    if return_target_sources is None:
        return_target_sources = defaultdict(list)
    cfg = networkx.DiGraph()
    if len(self._nodes) == 1:
        cfg.add_node(self._nodes[next(iter(self._nodes.keys()))])
    for tpl, targets in self._exit_targets.items():
        basic_block = self._nodes[tpl]
        for ex, jumpkind in targets:
            if ex in self._nodes:
                target_bbl = self._nodes[ex]
                cfg.add_edge(basic_block, target_bbl, jumpkind=jumpkind)
                if basic_block.addr in return_target_sources:
                    for src_irsb_key in return_target_sources[basic_block.addr
                        ]:
                        cfg.add_edge(self._nodes[src_irsb_key], basic_block,
                            jumpkind='Ijk_Ret')
            else:

                def addr_formalize(addr):
                    if addr is None:
                        return 'None'
                    else:
                        return '%#08x' % addr
                s = '(['
                for addr in ex[:-1]:
                    s += addr_formalize(addr) + ', '
                s += '] %s)' % addr_formalize(ex[-1])
                l.warning('Key %s does not exist.', s)
    return cfg