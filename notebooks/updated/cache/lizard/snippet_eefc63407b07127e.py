def get_county_estimates_by_state(self, api, table, variable, estimate, state):
    state = Division.objects.get(level=self.STATE_LEVEL, code=state)
    county_data = api.get(('NAME', estimate), {'for': 'county:*', 'in':
        'state:{}'.format(state.code)}, year=int(table.year))
    for datum in county_data:
        self.write_county_estimate(table, variable, estimate, datum)