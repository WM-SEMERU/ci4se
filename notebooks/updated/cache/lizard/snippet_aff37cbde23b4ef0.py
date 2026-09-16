def cleanup(self):
    for actor in self.actors:
        if actor.skip:
            continue
        actor.cleanup()
    super(ActorHandler, self).cleanup()