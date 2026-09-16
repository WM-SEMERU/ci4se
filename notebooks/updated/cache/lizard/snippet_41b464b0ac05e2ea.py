def release(self):
    if self.errored:
        self.pool.delete_resource(self)
    else:
        self.pool.release(self)