def layout(self, dimensions=None, **kwargs):
    return self.groupby(dimensions, container_type=NdLayout, **kwargs)