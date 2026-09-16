def location_query(self, value):
    del self.location_query
    queries = value.split('&')
    for q in queries:
        option = Option()
        option.number = defines.OptionRegistry.LOCATION_QUERY.number
        option.value = str(q)
        self.add_option(option)