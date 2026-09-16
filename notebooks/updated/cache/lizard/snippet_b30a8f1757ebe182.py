def free_resource_id(self, rid):
    self.resource_id_lock.acquire()
    try:
        i = rid & self.info.resource_id_mask
        if rid - i != self.info.resource_id_base:
            return None
        try:
            del self.resource_ids[i]
        except KeyError:
            pass
    finally:
        self.resource_id_lock.release()