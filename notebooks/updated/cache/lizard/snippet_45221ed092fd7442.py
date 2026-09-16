def sink_get(self, project, sink_name):
    path = 'projects/%s/sinks/%s' % (project, sink_name)
    sink_pb = self._gapic_api.get_sink(path)
    return MessageToDict(sink_pb)