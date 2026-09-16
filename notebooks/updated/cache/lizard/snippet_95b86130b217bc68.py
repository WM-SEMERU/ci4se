def save_relationship(self, relationship_form, *args, **kwargs):
    if relationship_form.is_for_update():
        return self.update_relationship(relationship_form, *args, **kwargs)
    else:
        return self.create_relationship(relationship_form, *args, **kwargs)