def _generate_base_mimetypes(self):
    for t in self.type_instances:
        if t.custom_mime:
            continue
        yield t.mime, (t, None, None)