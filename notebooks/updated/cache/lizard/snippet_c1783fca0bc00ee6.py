def runs(self, offset=0, limit=-1, properties=None):
    return get_run_listing(self.runs_url, offset=offset, limit=limit,
        properties=properties)