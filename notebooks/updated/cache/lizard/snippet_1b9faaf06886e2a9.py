def time_to_first_byte(self):
    if self.page_id == 'unknown':
        return None
    ttfb = 0
    for entry in self.entries:
        if entry['response']['status'] == 200:
            for k, v in iteritems(entry['timings']):
                if k != 'receive':
                    if v > 0:
                        ttfb += v
            break
        else:
            ttfb += entry['time']
    return ttfb