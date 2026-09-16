def imagej_metadata(self):
    if not self.is_imagej:
        return None
    page = self.pages[0]
    result = imagej_description_metadata(page.is_imagej)
    if 'IJMetadata' in page.tags:
        try:
            result.update(page.tags['IJMetadata'].value)
        except Exception:
            pass
    return result