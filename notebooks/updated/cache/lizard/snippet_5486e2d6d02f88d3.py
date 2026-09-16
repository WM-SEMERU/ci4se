def handle_json_GET_boundboxstops(self, params):
    schedule = self.server.schedule
    n = float(params.get('n'))
    e = float(params.get('e'))
    s = float(params.get('s'))
    w = float(params.get('w'))
    limit = int(params.get('limit'))
    stops = schedule.GetStopsInBoundingBox(north=n, east=e, south=s, west=w,
        n=limit)
    return [StopToTuple(s) for s in stops]