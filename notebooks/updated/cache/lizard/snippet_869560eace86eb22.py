def on_expired(self):
    print('Authentication expired')
    self.is_authenticating.acquire()
    self.is_authenticating.notify_all()
    self.is_authenticating.release()