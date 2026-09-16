def close(self):
    if self.stream is None:
        return
    try:
        self.stream.isatty()
        if self.stream.name in ['<stdin>', '<stdout>', '<stderr>']:
            return
    except AttributeError:
        pass
    except ValueError:
        pass
    try:
        from _pytest.compat import CaptureIO
        from _pytest.capture import EncodedFile
        if isinstance(self.stream, (CaptureIO, EncodedFile)):
            return
    except ImportError:
        pass
    try:
        from ipykernel.iostream import OutStream
        if isinstance(self.stream, OutStream):
            return
    except ImportError:
        pass
    try:
        self.stream.close()
    except AttributeError:
        self._logger.logger.warn(
            'the stream has no close method implementation: type={}'.format
            (type(self.stream)))
    finally:
        self._stream = None