def _duration_pb_to_timedelta(duration_pb):
    return datetime.timedelta(seconds=duration_pb.seconds, microseconds=
        duration_pb.nanos / 1000.0)