def initialize_openstack(func):

    async def wrap(self, *args, **kwargs):
        if not hasattr(self, 'auth') or not self.auth.is_token_valid():
            self.auth = AuthPassword(auth_url=self.config['auth_url'],
                username=self.config['username'], password=self.config[
                'password'], project_name=self.config['project_name'],
                user_domain_name=self.config['user_domain_name'],
                project_domain_name=self.config['project_domain_name'])
            self.nova = NovaClient(session=self.auth)
            self.glance = GlanceClient(session=self.auth)
            await self.nova.init_api(timeout=self.config.get('http_timeout',
                10))
            await self.glance.init_api(timeout=self.config.get(
                'http_timeout', 10))
        if not hasattr(self, 'last_init') or self.last_init < time.time() - 60:
            await self.initialize()
            self.last_init = time.time()
        return await func(self, *args, **kwargs)
    return wrap