def save(self, *args, **kwargs):
    self.perform_bulk_pubmed_query()
    super().save(*args, **kwargs)