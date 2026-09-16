def replace(self, refobj, reference, taskfileinfo):
    jbfile = JB_File(taskfileinfo)
    filepath = jbfile.get_fullpath()
    cmds.file(filepath, loadReference=reference)
    ns = cmds.referenceQuery(reference, namespace=True)
    content = cmds.namespaceInfo(ns, listOnlyDependencyNodes=True, dagPath=True
        )
    scenenode = self.get_scenenode(content)
    self.get_refobjinter().connect_reftrack_scenenode(refobj, scenenode)