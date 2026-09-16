def rsl_dump_stream_begin(self, stream_id):
    err, err2, count = self.sensor_log.dump_begin(stream_id)
    return [err, err2, count, 0]