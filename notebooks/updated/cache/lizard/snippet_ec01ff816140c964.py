def getProjectAreaByID(self, projectarea_id, archived=False,
    returned_properties=None):
    if not isinstance(projectarea_id, six.string_types) or not projectarea_id:
        excp_msg = 'Please specify a valid ProjectArea ID'
        self.log.error(excp_msg)
        raise exception.BadValue(excp_msg)
    self.log.debug('Try to get <ProjectArea> by its id: %s', projectarea_id)
    rp = returned_properties
    proj_areas = self._getProjectAreas(archived=archived,
        returned_properties=rp, projectarea_id=projectarea_id)
    if proj_areas is not None:
        proj_area = proj_areas[0]
        self.log.info('Find <ProjectArea %s>', proj_area)
        return proj_area
    self.log.error("No ProjectArea's ID is %s", projectarea_id)
    raise exception.NotFound("No ProjectArea's ID is %s" % projectarea_id)