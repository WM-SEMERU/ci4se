def get_instance(self):
    try:
        return self._instance
    except AttributeError:
        self._instance = self._decorated()
        return self._instance