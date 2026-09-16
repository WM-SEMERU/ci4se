def values(self, column_name, exclude_type=STRUCT):
    column_name = unnest_path(column_name)
    columns = self.columns
    output = []
    for path in self.query_path:
        full_path = untype_path(concat_field(path, column_name))
        for c in columns:
            if c.jx_type in exclude_type:
                continue
            if untype_path(c.name) == full_path:
                output.append(c)
        if output:
            return output
    return []