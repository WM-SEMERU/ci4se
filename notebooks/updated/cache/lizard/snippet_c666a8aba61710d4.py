def start(self):
    if self.address != 'localhost':
        raise ModHostError(
            'The host configured in the constructor isnt "localhost". It is not possible to start a process on another device.'
            )
    try:
        subprocess.call([self.process, '-p', str(self.port)])
    except FileNotFoundError as e:
        exception = ModHostError(
            'mod-host not found. Did you install it? (https://github.com/moddevices/mod-host#building)'
            )
        raise exception from e
    self._started_with_this_api = True