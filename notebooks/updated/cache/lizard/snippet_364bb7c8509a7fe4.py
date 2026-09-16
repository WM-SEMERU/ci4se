def write(self, document, obj, *args, **kwargs):
    try:
        document = IWritableDocument(document)
        mime_type = document.mime_type
        writer = self.lookup_writer(mime_type, obj)
        if not writer:
            msg = 'No adapter found to write object %s to %s document' % (obj
                .__class__.__name__, mime_type)
            raise NoWriterFoundError(msg)
        return writer.write(document, obj, *args, **kwargs)
    except:
        return defer.fail(Failure())