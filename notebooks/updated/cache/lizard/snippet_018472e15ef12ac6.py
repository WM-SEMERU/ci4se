def StreamMedia(self, callback=None, finish_callback=None,
    additional_headers=None):
    return self.__StreamMedia(callback=callback, finish_callback=
        finish_callback, additional_headers=additional_headers, use_chunks=
        False)