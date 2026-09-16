def find_dvs_by_path(self, si, path):
    dvs = self.get_folder(si, path)
    if not dvs:
        raise ValueError('Could not find Default DvSwitch in path {0}'.
            format(path))
    elif not isinstance(dvs, vim.dvs.VmwareDistributedVirtualSwitch):
        raise ValueError('The object in path {0} is {1} and not a DvSwitch'
            .format(path, type(dvs)))
    return dvs