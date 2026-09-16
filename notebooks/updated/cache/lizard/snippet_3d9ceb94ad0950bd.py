def getAction(self, action_name):
    self.log.debug('Try to get <Action %s>', action_name)
    if not isinstance(action_name, six.string_types) or not action_name:
        excp_msg = 'Please specify a valid action name'
        self.log.error(excp_msg)
        raise exception.BadValue(excp_msg)
    actions = self._getActions(action_name=action_name)
    if actions is not None:
        action = actions[0]
        self.log.info('Find <Action %s>', action)
        return action
    self.log.error('No Action named %s', action_name)
    raise exception.NotFound('No Action named %s' % action_name)