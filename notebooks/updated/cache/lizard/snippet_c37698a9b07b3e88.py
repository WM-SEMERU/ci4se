def subscribe(self, topic, options=None):

    def decorator(func):
        if self._started:
            self.session.subscribe(handler=func, topic=topic, options=options)
        else:

            def subscriber():
                self.session.subscribe(handler=func, topic=topic, options=
                    options)
            self._on_running_callbacks.append(subscriber)
        return func
    return decorator