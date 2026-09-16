def create_router(self, context, router):
    new_router = super(AristaL3ServicePlugin, self).create_router(context,
        router)
    try:
        self.driver.create_router(context, new_router)
        return new_router
    except Exception:
        with excutils.save_and_reraise_exception():
            LOG.error(_LE('Error creating router on Arista HW router=%s '),
                new_router)
            super(AristaL3ServicePlugin, self).delete_router(context,
                new_router['id'])