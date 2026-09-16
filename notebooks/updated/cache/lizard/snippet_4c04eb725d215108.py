def save(self, *args, **kwargs):
    name_max_len = self._meta.get_field('name').max_length
    if len(self.name) > name_max_len:
        self.name = self.name[:name_max_len - 3] + '...'
    for _ in range(MAX_SLUG_RETRIES):
        try:
            with transaction.atomic():
                super().save(*args, **kwargs)
                break
        except IntegrityError as error:
            if '{}_slug'.format(self._meta.db_table) in error.args[0]:
                self.slug = None
                continue
            raise
    else:
        raise IntegrityError(
            'Maximum number of retries exceeded during slug generation')