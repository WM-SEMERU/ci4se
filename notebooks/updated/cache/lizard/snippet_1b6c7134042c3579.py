def publish(self, object_id: str, event_type: str, event_data: dict=None):
    object_key = SchedulingObject.get_key(self.type, object_id)
    publish(event_type=event_type, event_data=event_data, object_type=self.
        type, object_id=object_id, object_key=object_key, origin=None)