def register(self, observer):
    self.observer_manager.append(observer)
    observer.manager = self