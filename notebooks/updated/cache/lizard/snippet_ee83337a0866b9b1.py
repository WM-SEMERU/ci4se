def download_spt_forecast(self, extract_directory):
    needed_vars = (self.spt_watershed_name, self.spt_subbasin_name, self.
        spt_forecast_date_string, self.ckan_engine_url, self.ckan_api_key,
        self.ckan_owner_organization)
    if None not in needed_vars:
        er_manager = ECMWFRAPIDDatasetManager(self.ckan_engine_url, self.
            ckan_api_key, self.ckan_owner_organization)
        er_manager.download_prediction_dataset(watershed=self.
            spt_watershed_name, subbasin=self.spt_subbasin_name,
            date_string=self.spt_forecast_date_string, extract_directory=
            extract_directory)
        return glob(os.path.join(extract_directory, self.
            spt_forecast_date_string, 'Qout*52.nc'))[0]
    elif needed_vars.count(None) == len(needed_vars):
        log.info('Skipping streamflow forecast download ...')
        return None
    else:
        raise ValueError(
            """To download the forecasts, you need to set: 
spt_watershed_name, spt_subbasin_name, spt_forecast_date_string 
ckan_engine_url, ckan_api_key, and ckan_owner_organization."""
            )