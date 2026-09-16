def pipeline_url(self):
    return PipelineEntity.get_url(server_url=self._session.server_url,
        pipeline_name=self.data.name)