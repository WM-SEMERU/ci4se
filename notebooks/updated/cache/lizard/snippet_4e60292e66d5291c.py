def _parse_uptime_string(self, uptime):
    uptime = uptime.strip()
    load_averages = uptime[uptime.find('load average:'):].split(':')[1].split(
        ',')
    uptime_sec = uptime.split(',')[0]
    return {'loads': list(map(float, load_averages)), 'uptime_sec': uptime_sec}