def visualize(self, filename='mydask', format=None, **kwargs):
    check_is_fitted(self, 'dask_graph_')
    return dask.visualize(self.dask_graph_, filename=filename, format=
        format, **kwargs)