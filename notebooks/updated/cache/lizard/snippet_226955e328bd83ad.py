def execute_tool(self, stream, interval):
    if interval.end > self.up_to_timestamp:
        raise ValueError('The stream is not available after ' + str(self.
            up_to_timestamp) + ' and cannot be calculated')
    required_intervals = TimeIntervals([interval]
        ) - stream.calculated_intervals
    if not required_intervals.is_empty:
        for interval in required_intervals:
            stream.tool.execute(stream.input_streams, stream, interval)
            stream.calculated_intervals += interval
        if not stream.required_intervals.is_empty:
            raise RuntimeError(
                'Tool execution did not cover the specified time interval.')