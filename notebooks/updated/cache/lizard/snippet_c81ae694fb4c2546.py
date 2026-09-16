def set_status(self, new_status, notes=None):
    self.status_id = new_status
    try:
        self.status['id'] = self.status_id
        self.status['name'] = None
    except:
        pass
    self.save(notes)