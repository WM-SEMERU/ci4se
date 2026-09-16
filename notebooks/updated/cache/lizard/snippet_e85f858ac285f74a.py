def parseEvent(self, result, i):
    fmt = '%Y-%m-%dT%H:%M:%SZ'
    due = 0
    delay = 0
    real_time = 'n'
    number = result['stopEvents'][i]['transportation']['number']
    planned = datetime.strptime(result['stopEvents'][i][
        'departureTimePlanned'], fmt)
    destination = result['stopEvents'][i]['transportation']['destination'][
        'name']
    mode = self.get_mode(result['stopEvents'][i]['transportation'][
        'product']['class'])
    estimated = planned
    if 'isRealtimeControlled' in result['stopEvents'][i]:
        real_time = 'y'
        estimated = datetime.strptime(result['stopEvents'][i][
            'departureTimeEstimated'], fmt)
    if estimated > datetime.utcnow():
        due = self.get_due(estimated)
        delay = self.get_delay(planned, estimated)
        return [number, due, delay, planned, estimated, real_time,
            destination, mode]
    else:
        return None