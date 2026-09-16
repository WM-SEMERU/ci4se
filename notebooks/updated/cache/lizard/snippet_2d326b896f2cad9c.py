def _push_tail(self, level, parent, tail_node):
    ret = list(parent)
    if level == SHIFT:
        ret.append(tail_node)
        return ret
    sub_index = self._count - 1 >> level & BIT_MASK
    if len(parent) > sub_index:
        ret[sub_index] = self._push_tail(level - SHIFT, parent[sub_index],
            tail_node)
        return ret
    ret.append(self._new_path(level - SHIFT, tail_node))
    return ret