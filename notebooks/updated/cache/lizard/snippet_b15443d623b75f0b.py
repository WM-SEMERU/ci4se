def _assert_link_secret(self, action: str):
    if self._link_secret is None:
        LOGGER.debug(
            'HolderProver._assert_link_secret: action %s requires link secret but it is not set'
            , action)
        raise AbsentLinkSecret(
            'Action {} requires link secret but it is not set'.format(action))