def getPlannedFor(self, plannedfor_name, projectarea_id=None,
    projectarea_name=None, archived=False, returned_properties=None):
    if not isinstance(plannedfor_name, six.string_types
        ) or not plannedfor_name:
        excp_msg = 'Please specify a valid PlannedFor name'
        self.log.error(excp_msg)
        raise exception.BadValue(excp_msg)
    self.log.debug('Try to get <PlannedFor %s>', plannedfor_name)
    rp = returned_properties
    plannedfors = self._getPlannedFors(projectarea_id=projectarea_id,
        projectarea_name=projectarea_name, archived=archived,
        returned_properties=rp, plannedfor_name=plannedfor_name)
    if plannedfors is not None:
        plannedfor = plannedfors[0]
        self.log.info('Find <PlannedFor %s>', plannedfor)
        return plannedfor
    self.log.error('No PlannedFor named %s', plannedfor_name)
    raise exception.NotFound('No PlannedFor named %s' % plannedfor_name)