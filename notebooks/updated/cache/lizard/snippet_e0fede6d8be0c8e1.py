def wrap_scene(cls, root, refobjinter):
    refobjects = cls.get_unwrapped(root, refobjinter)
    tracks = cls.wrap(root, refobjinter, refobjects)
    sugs = root.get_scene_suggestions(refobjinter)
    for typ, element in sugs:
        r = cls(root=root, refobjinter=refobjinter, typ=typ, element=element)
        tracks.append(r)
    return tracks