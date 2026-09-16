def copy(self, deep=True):
    thistype = type(self)
    newobject = thistype()
    if deep:
        newobject.DeepCopy(self)
    else:
        newobject.ShallowCopy(self)
    newobject.copy_meta_from(self)
    return newobject