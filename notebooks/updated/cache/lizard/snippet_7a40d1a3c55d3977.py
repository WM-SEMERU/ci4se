def annotate_from_changeset(self, changeset):
    if self.annotate_from_changeset_func:
        return self.annotate_from_changeset_func(changeset)
    else:
        return ''.join((changeset.id, '\n'))