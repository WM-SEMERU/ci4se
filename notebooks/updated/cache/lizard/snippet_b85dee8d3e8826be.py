def save(self, model, commit=True):
    self.is_instance(model)
    db.session.add(model)
    if commit:
        db.session.commit()
    return model