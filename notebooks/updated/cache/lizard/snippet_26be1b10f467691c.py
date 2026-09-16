def get_least_common_subsumer(self, from_tid, to_tid):
    termid_from = self.terminal_for_term.get(from_tid)
    termid_to = self.terminal_for_term.get(to_tid)
    path_from = self.paths_for_terminal[termid_from][0]
    path_to = self.paths_for_terminal[termid_to][0]
    common_nodes = set(path_from) & set(path_to)
    if len(common_nodes) == 0:
        return None
    else:
        indexes = []
        for common_node in common_nodes:
            index1 = path_from.index(common_node)
            index2 = path_to.index(common_node)
            indexes.append((common_node, index1 + index2))
        indexes.sort(key=itemgetter(1))
        shortest_common = indexes[0][0]
        return shortest_common