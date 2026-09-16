def onGamePlayed(self, mid=None, author_id=None, game_id=None, game_name=
    None, score=None, leaderboard=None, thread_id=None, thread_type=None,
    ts=None, metadata=None, msg=None):
    log.info('{} played "{}" in {} ({})'.format(author_id, game_name,
        thread_id, thread_type.name))