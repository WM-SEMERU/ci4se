def pipeline_output(self, name):
    try:
        pipe, chunks, _ = self._pipelines[name]
    except KeyError:
        raise NoSuchPipeline(name=name, valid=list(self._pipelines.keys()))
    return self._pipeline_output(pipe, chunks, name)