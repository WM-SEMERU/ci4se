def remove_child(self, router):
    if router in self.routes:
        self.routes.remove(router)
        router._parent = None