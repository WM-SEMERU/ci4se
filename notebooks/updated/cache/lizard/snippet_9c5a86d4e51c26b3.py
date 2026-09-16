def fetch_state_data(self, states):
    print('Fetching census data')
    for table in CensusTable.objects.all():
        api = self.get_series(table.series)
        for variable in table.variables.all():
            estimate = '{}_{}'.format(table.code, variable.code)
            print('>> Fetching {} {} {}'.format(table.year, table.series,
                estimate))
            for state in tqdm(states):
                self.get_state_estimates_by_state(api=api, table=table,
                    variable=variable, estimate=estimate, state=state)
                self.get_county_estimates_by_state(api=api, table=table,
                    variable=variable, estimate=estimate, state=state)
                self.get_district_estimates_by_state(api=api, table=table,
                    variable=variable, estimate=estimate, state=state)