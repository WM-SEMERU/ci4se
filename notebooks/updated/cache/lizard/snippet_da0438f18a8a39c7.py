def _full_pipeline(self):
    options = self._pipeline_options()
    full_pipeline = [{'$changeStream': options}]
    full_pipeline.extend(self._pipeline)
    return full_pipeline