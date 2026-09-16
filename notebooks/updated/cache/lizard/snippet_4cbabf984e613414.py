def running_objects(self):
    return [obj for obj in self.database_objects if obj.status in [obj.
        known_statuses.RUNNING]]