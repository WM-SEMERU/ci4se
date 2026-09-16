def get_tags(self, view_object=None):
    tags = [force_unicode(self.bundle.get_title())]
    back_bundle = self.get_back_bundle()
    if back_bundle and back_bundle != self.bundle:
        tags.append(force_unicode(back_bundle.get_title()))
    if view_object:
        tags.append(force_unicode(view_object))
    return tags