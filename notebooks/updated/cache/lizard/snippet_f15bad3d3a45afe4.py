def connect_reftrack_scenenode(self, refobj, scenenode):
    conns = [('%s.scenenode' % refobj, '%s.reftrack' % scenenode), (
        '%s.taskfile_id' % scenenode, '%s.taskfile_id' % refobj)]
    for src, dst in conns:
        if not cmds.isConnected(src, dst):
            cmds.connectAttr(src, dst, force=True)