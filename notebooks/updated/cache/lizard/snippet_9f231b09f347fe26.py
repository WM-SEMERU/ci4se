def parse(self):
    try:
        self.parsed_data = json.loads(self.data)
    except UnicodeError as e:
        self.parsed_data = json.loads(self.data.decode('latin1'))
    except Exception as e:
        raise Exception(
            'Error while converting response from JSON to python. %s' % e)
    if self.parsed_data.get('type', '') != 'FeatureCollection':
        raise Exception(
            'GeoJson synchronizer expects a FeatureCollection object at root level'
            )
    self.parsed_data = self.parsed_data['features']