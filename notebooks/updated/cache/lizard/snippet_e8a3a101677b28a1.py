def notify_all(self):
    self.condition.acquire()
    try:
        self.condition.notify_all()
    except:
        self.condition.notifyAll()
    self.condition.release()