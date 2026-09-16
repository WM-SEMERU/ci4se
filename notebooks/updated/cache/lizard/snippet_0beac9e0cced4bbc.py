def attach_pipeline(self, pipeline, name, chunks=None, eager=True):
    if chunks is None:
        chunks = chain([5], repeat(126))
    elif isinstance(chunks, int):
        chunks = repeat(chunks)
    if name in self._pipelines:
        raise DuplicatePipelineName(name=name)
    self._pipelines[name] = AttachedPipeline(pipeline, iter(chunks), eager)
    return pipeline