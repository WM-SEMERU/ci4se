def create(self, image=None):
    container = self.context
    new = api.content.create(container=container, type=self.portal_type,
        title=self.title, safe_id=True)
    if image:
        namedblobimage = NamedBlobImage(data=image.read(), filename=
            safe_unicode(image.filename))
        new.image = namedblobimage
    if new:
        new.description = safe_unicode(self.description)
        return new.absolute_url()