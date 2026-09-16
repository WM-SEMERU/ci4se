def door(idf, fsdobject, deletebsd=True, setto000=False):
    if fsdobject.Surface_Type.upper() == 'DOOR':
        simpleobject = idf.newidfobject('DOOR')
        simpleobject.Name = fsdobject.Name
        simpleobject.Construction_Name = fsdobject.Construction_Name
        simpleobject.Building_Surface_Name = fsdobject.Building_Surface_Name
        simpleobject.Multiplier = fsdobject.Multiplier
        surforigin = fsdorigin(fsdobject, setto000=setto000)
        simpleobject.Starting_X_Coordinate = surforigin[0]
        simpleobject.Starting_Z_Coordinate = surforigin[1]
        simpleobject.Length = fsdobject.width
        simpleobject.Height = fsdobject.height
        if deletebsd:
            idf.removeidfobject(fsdobject)
        return simpleobject
    return None