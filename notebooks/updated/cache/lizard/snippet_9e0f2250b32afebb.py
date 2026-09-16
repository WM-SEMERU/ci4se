def allocate(self):
    self.lock.acquire()
    try:
        id_ = self.next_id
        self.next_id += 1
        return id_
    finally:
        self.lock.release()