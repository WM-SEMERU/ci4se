def save(self, role, commit=True):
    self.is_instance(role)
    schema = RoleSchema()
    valid = schema.process(role)
    if not valid:
        return valid
    db.session.add(role)
    if commit:
        db.session.commit()
    events.role_saved_event.send(role)
    return role