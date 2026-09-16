async def self_check(cls):
    async for check in super().self_check():
        yield check
    s = cls.settings()
    if not hasattr(settings, 'BERNARD_BASE_URL'):
        yield HealthCheckFail('00005',
            '"BERNARD_BASE_URL" cannot be found in the configuration. TheTelegram platform needs it because it uses it to automatically register its hook.'
            )
    if not hasattr(settings, 'WEBVIEW_SECRET_KEY'):
        yield HealthCheckFail('00005',
            '"WEBVIEW_SECRET_KEY" cannot be found in the configuration. It is required in order to be able to create secure postback URLs.'
            )