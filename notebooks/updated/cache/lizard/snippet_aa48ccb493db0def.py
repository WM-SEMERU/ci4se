def delete(self, role, commit=True):
    events.role_deleted_event.send(role)
    return super().delete(role, commit)