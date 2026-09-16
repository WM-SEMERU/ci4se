def timeline_home(self, max_id=None, min_id=None, since_id=None, limit=None):
    return self.timeline('home', max_id=max_id, min_id=min_id, since_id=
        since_id, limit=limit)