def updated_by(self):
    if self.api and self.updated_by_id:
        return self.api._get_user(self.updated_by_id)