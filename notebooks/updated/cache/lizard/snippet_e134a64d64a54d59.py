def children(self, unroll=False, skip_not_present=True):
    for child_inst in self.inst.children:
        if skip_not_present:
            if not child_inst.properties.get('ispresent', True):
                continue
        if unroll and isinstance(child_inst, comp.AddressableComponent
            ) and child_inst.is_array:
            range_list = [range(n) for n in child_inst.array_dimensions]
            for idxs in itertools.product(*range_list):
                N = Node._factory(child_inst, self.env, self)
                N.current_idx = idxs
                yield N
        else:
            yield Node._factory(child_inst, self.env, self)