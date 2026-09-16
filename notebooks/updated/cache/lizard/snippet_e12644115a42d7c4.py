def get_analysis(self):
    if self.analysis_url:
        try:
            try:
                json_string = urllib2.urlopen(self.analysis_url).read()
            except urllib2.HTTPError:
                param_dict = dict(id=self.id)
                new_track = _profile(param_dict, DEFAULT_ASYNC_TIMEOUT)
                if new_track and new_track.analysis_url:
                    self.analysis_url = new_track.analysis_url
                    json_string = urllib2.urlopen(self.analysis_url).read()
                else:
                    raise Exception('Failed to create track analysis.')
            analysis = json.loads(json_string)
            analysis_track = analysis.pop('track', {})
            self.__dict__.update(analysis)
            self.__dict__.update(analysis_track)
        except Exception:
            raise Exception('Failed to create track analysis.')
    else:
        raise Exception('Failed to create track analysis.')