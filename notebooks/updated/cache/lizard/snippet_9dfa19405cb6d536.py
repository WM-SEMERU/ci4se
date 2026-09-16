def enter_room(self, sid, room, namespace=None):
    namespace = namespace or '/'
    self.logger.info('%s is entering room %s [%s]', sid, room, namespace)
    self.manager.enter_room(sid, namespace, room)