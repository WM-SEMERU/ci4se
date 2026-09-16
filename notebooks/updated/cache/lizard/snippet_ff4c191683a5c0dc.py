def GetStream(data=None):
    if len(__mstreams_available__) == 0:
        if data:
            mstream = MemoryStream(data)
            mstream.seek(0)
        else:
            mstream = MemoryStream()
        __mstreams__.append(mstream)
        return mstream
    mstream = __mstreams_available__.pop()
    if data is not None and len(data):
        mstream.Cleanup()
        mstream.write(data)
    mstream.seek(0)
    return mstream