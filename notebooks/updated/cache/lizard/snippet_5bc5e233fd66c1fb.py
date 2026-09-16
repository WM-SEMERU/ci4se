def save(self, *args, **kwargs):
    self.text = clean_text(self.text)
    self.text_formatted = format_text(self.text)
    super(BaseUserContentModel, self).save(*args, **kwargs)