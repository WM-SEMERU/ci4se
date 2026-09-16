def _handle_dump(self, handler, file_object, **kwargs):
    return handler.dump(self.__class__, to_dict(self), file_object, **kwargs)