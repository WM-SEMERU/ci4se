def config(self):
    return PipelineConfigManager(session=self._session, pipeline_name=self.
        data.name)