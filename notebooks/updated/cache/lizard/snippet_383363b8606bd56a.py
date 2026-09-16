def get_current_scene_node():
    c = cmds.namespaceInfo(':', listOnlyDependencyNodes=True, absoluteName=
        True, dagPath=True)
    l = cmds.ls(c, type='jb_sceneNode', absoluteName=True)
    if not l:
        return
    else:
        for n in sorted(l):
            if not cmds.listConnections('%s.reftrack' % n, d=False):
                return n