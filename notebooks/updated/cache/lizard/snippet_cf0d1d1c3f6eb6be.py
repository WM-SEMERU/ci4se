def find_family(self, pattern='.*', flags=0, node=None):
    return [node for node in foundations.walkers.nodes_walker(node or self) if
        re.search(pattern, node.family, flags)]