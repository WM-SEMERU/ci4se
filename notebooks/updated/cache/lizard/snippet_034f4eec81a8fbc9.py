def reject(self, *, requeue=True):
    self.sender.send_BasicReject(self.delivery_tag, requeue)