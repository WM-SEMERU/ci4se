def get_obj(self, vimtype, name, folder=None):
    obj = None
    content = self.service_instance.RetrieveContent()
    if folder is None:
        folder = content.rootFolder
    container = content.viewManager.CreateContainerView(folder, [vimtype], True
        )
    for c in container.view:
        if c.name == name:
            obj = c
            break
    container.Destroy()
    return obj