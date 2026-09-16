def id_pseudopath(self):
    try:
        pseudopath = Fields(str(self.value[auto_id_field]))
    except (TypeError, AttributeError, KeyError):
        pseudopath = self.path
    if self.context:
        return self.context.id_pseudopath.child(pseudopath)
    else:
        return pseudopath