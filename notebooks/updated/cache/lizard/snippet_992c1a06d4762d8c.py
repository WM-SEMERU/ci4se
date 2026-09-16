def actors(self, actors):
    if actors is None:
        actors = self.default_actors()
    self.check_actors(actors)
    self.config['actors'] = actors