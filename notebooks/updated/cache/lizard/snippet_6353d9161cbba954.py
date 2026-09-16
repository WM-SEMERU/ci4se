def delete(filething):
    t = OggFLAC(filething)
    filething.fileobj.seek(0)
    t.delete(filething)