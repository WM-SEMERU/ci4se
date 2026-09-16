def cloud_cover_to_irradiance(self, cloud_cover, how='clearsky_scaling', **
    kwargs):
    how = how.lower()
    if how == 'clearsky_scaling':
        irrads = self.cloud_cover_to_irradiance_clearsky_scaling(cloud_cover,
            **kwargs)
    elif how == 'liujordan':
        irrads = self.cloud_cover_to_irradiance_liujordan(cloud_cover, **kwargs
            )
    else:
        raise ValueError('invalid how argument')
    return irrads