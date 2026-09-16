def initialize(self):
    if not self._initialized:
        logger.info('initializing %r', self)
        if not os.path.exists(self.path):
            if self.mode is not None:
                os.makedirs(self.path, mode=self.mode)
            else:
                os.makedirs(self.path)
        self._set_mode()
        self._add_facl_rules()
        self._set_selinux_context()
        self._set_ownership()
        self._initialized = True
        logger.info('initialized')
        return
    logger.info('%r was already initialized', self)