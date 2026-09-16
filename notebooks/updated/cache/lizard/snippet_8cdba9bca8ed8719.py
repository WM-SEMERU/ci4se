def add(self, full_name, repetition_type, type):
    base_name = self.element.name
    simple_name = relative_field(full_name, base_name)
    path = split_field(simple_name)
    output = self
    if len(path) == 0:
        return output._add_one('.', full_name, repetition_type, type)
    else:
        fname = base_name
        for p in path[:-1]:
            fname = concat_field(fname, p)
            n = output.more.get(p)
            output = n or output._add_one(p, fname, OPTIONAL, object)
        return output._add_one(path[-1], full_name, repetition_type, type)