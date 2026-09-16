def integrate_storage(self, timeseries, position, **kwargs):
    StorageControl(edisgo=self, timeseries=timeseries, position=position,
        **kwargs)