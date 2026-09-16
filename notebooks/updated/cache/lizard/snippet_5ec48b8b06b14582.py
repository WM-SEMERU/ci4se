def find_by_path(self, path):
    pathparts = path.split('.')
    current_node = self
    for pathpart in pathparts:
        m = re.fullmatch('^(\\w+)((?:\\[(?:\\d+|0[xX][\\da-fA-F]+)\\])*)$',
            pathpart)
        if not m:
            raise ValueError('Invalid path')
        inst_name, array_suffix = m.group(1, 2)
        idx_list = [int(s, 0) for s in re.findall(
            '\\[(\\d+|0[xX][\\da-fA-F]+)\\]', array_suffix)]
        current_node = current_node.get_child_by_name(inst_name)
        if current_node is None:
            return None
        if idx_list:
            if isinstance(current_node, AddressableNode
                ) and current_node.inst.is_array:
                if len(idx_list) != len(current_node.inst.array_dimensions):
                    raise IndexError('Wrong number of array dimensions')
                current_node.current_idx = []
                for i, idx in enumerate(idx_list):
                    if idx >= current_node.inst.array_dimensions[i]:
                        raise IndexError('Array index out of range')
                    current_node.current_idx.append(idx)
            else:
                raise IndexError('Index attempted on non-array component')
    return current_node