def clone(self, project, folder='/', **kwargs):
    if self._proj is None:
        raise DXError(
            'Clone called when a project ID was not associated with this object handler'
            )
    dxpy.api.project_clone(self._proj, {'objects': [self._dxid], 'project':
        project, 'destination': folder}, **kwargs)
    cloned_copy = copy.copy(self)
    cloned_copy.set_ids(cloned_copy.get_id(), project)
    return cloned_copy