def release(self, resource):
    with self.releaser:
        resource.claimed = False
        self.releaser.notify_all()