def make_timebar(progress=0, duration=0):
    duration_string = api_music.duration_to_string(duration)
    if duration <= 0:
        return '---'
    time_counts = int(round(progress / duration * TIMEBAR_LENGTH))
    if time_counts > TIMEBAR_LENGTH:
        time_counts = TIMEBAR_LENGTH
    if duration > 0:
        bar = '│' + TIMEBAR_PCHAR * time_counts + TIMEBAR_ECHAR * (
            TIMEBAR_LENGTH - time_counts) + '│'
        time_bar = '{} {}'.format(bar, duration_string)
    else:
        time_bar = duration_string
    return time_bar