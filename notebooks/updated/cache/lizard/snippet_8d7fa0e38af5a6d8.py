def update_check(self, existing, new):
    old_state = existing.state
    if 'NowPlayingItem' in existing.session_raw:
        try:
            old_theme = existing.session_raw['NowPlayingItem']['IsThemeMedia']
        except KeyError:
            old_theme = False
    else:
        old_theme = False
    if 'NowPlayingItem' in new:
        if new['PlayState']['IsPaused']:
            new_state = STATE_PAUSED
        else:
            new_state = STATE_PLAYING
        try:
            new_theme = new['NowPlayingItem']['IsThemeMedia']
        except KeyError:
            new_theme = False
    else:
        new_state = STATE_IDLE
        new_theme = False
    if old_theme or new_theme:
        return False
    elif old_state == STATE_PLAYING or new_state == STATE_PLAYING:
        return True
    elif old_state != new_state:
        return True
    else:
        return False