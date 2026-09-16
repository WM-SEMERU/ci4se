def load_forecasts(self):
    forecast_path = self.forecast_json_path + '/{0}/{1}/'.format(self.
        run_date.strftime('%Y%m%d'), self.ensemble_member)
    forecast_files = sorted(glob(forecast_path + '*.json'))
    for forecast_file in forecast_files:
        file_obj = open(forecast_file)
        json_obj = json.load(file_obj)
        file_obj.close()
        track_id = json_obj['properties']['id']
        obs_track_id = json_obj['properties']['obs_track_id']
        forecast_hours = json_obj['properties']['times']
        duration = json_obj['properties']['duration']
        for f, feature in enumerate(json_obj['features']):
            area = np.sum(feature['properties']['masks'])
            step_id = track_id + '_{0:02d}'.format(f)
            for model_type in self.model_types:
                for model_name in self.model_names[model_type]:
                    prediction = feature['properties'][model_type + '_' +
                        model_name.replace(' ', '-')]
                    if model_type == 'condition':
                        prediction = [prediction]
                    row = [track_id, obs_track_id, self.ensemble_name, self
                        .ensemble_member, forecast_hours[f], f + 1,
                        duration, area] + prediction
                    self.forecasts[model_type][model_name].loc[step_id] = row