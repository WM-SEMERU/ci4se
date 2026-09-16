def import_image_from_file(self, filename, repository=None, tag=None,
    changes=None):
    return self.import_image(src=filename, repository=repository, tag=tag,
        changes=changes)