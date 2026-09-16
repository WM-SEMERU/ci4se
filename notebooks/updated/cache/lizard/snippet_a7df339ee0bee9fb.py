def init(ffi, lib):


    class RingBuffer(_RingBufferBase):
        __doc__ = _RingBufferBase.__doc__
        _ffi = ffi
        _lib = lib
    return RingBuffer