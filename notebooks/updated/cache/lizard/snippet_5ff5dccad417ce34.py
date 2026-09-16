def flush(self):
    annotation = self.get_annotation()
    if annotation.get(ATTACHMENTS_STORAGE) is not None:
        del annotation[ATTACHMENTS_STORAGE]