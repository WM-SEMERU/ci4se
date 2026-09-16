def get_parsed_sked(self, skedname):
    if not self.processed:
        raise Exception('Filing must be processed to return parsed sked')
    if skedname in self.schedules:
        matching_skeds = []
        for sked in self.result:
            if sked['schedule_name'] == skedname:
                matching_skeds.append(sked)
        return matching_skeds
    else:
        return []