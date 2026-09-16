def _save_table(self, raw=False, cls=None, force_insert=False, force_update
    =False, using=None, update_fields=None):
    updated = super(ModelMixin, self)._save_table(raw=raw, cls=cls,
        force_insert=force_insert, force_update=force_update, using=using,
        update_fields=update_fields)
    self._linguist.decider.objects.save_translations([self])
    return updated