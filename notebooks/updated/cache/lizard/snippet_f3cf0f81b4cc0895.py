def saveTemplate(self):
    savedict = {}
    for comp_editor in self.widgets():
        stim = comp_editor.component()
        comp_editor.saveToObject()
        savedict[stim.name] = stim.stateDict()
    savedict['delay'] = self.delaySpnbx.value()
    return savedict