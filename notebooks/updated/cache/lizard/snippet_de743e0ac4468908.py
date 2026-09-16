def dframe(self, dimensions=None, multi_index=False):
    import pandas as pd
    if dimensions is None:
        dimensions = [d.name for d in self.dimensions()]
    else:
        dimensions = [self.get_dimension(d, strict=True).name for d in
            dimensions]
    column_names = dimensions
    dim_vals = OrderedDict([(dim, self.dimension_values(dim)) for dim in
        column_names])
    df = pd.DataFrame(dim_vals)
    if multi_index:
        df = df.set_index([d for d in dimensions if d in self.kdims])
    return df