def update_groups_for_state(self, state: State):
    users = get_users_for_state(state)
    for config in self.filter(states=state):
        logger.debug('in state loop')
        for user in users:
            logger.debug('in user loop for {}'.format(user))
            config.update_group_membership_for_user(user)