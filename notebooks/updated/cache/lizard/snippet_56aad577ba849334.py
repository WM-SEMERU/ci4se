def save(self, *args, **kwargs):
    now = datetime.utcnow().replace(tzinfo=pytz.UTC)
    if not self.pk:
        self.created = now
    self.modified = now
    return super(Configuration, self).save(*args, **kwargs)