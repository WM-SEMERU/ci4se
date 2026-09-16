def losc_frame_urls(ifo, start_time, end_time):
    data = losc_frame_json(ifo, start_time, end_time)['strain']
    return [d['url'] for d in data if d['format'] == 'gwf']