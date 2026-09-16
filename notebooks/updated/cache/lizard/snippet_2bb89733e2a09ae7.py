def zone_floor2roofheight(idf, zonename, debug=False):
    zone = idf.getobject('ZONE', zonename)
    surfs = idf.idfobjects['BuildingSurface:Detailed'.upper()]
    zone_surfs = [s for s in surfs if s.Zone_Name == zone.Name]
    floors = [s for s in zone_surfs if s.Surface_Type.upper() == 'FLOOR']
    roofs = [s for s in zone_surfs if s.Surface_Type.upper() == 'ROOF']
    ceilings = [s for s in zone_surfs if s.Surface_Type.upper() == 'CEILING']
    topsurfaces = roofs + ceilings
    topz = []
    for topsurface in topsurfaces:
        for coord in topsurface.coords:
            topz.append(coord[-1])
    topz = max(topz)
    botz = []
    for floor in floors:
        for coord in floor.coords:
            botz.append(coord[-1])
    botz = min(botz)
    height = topz - botz
    return height