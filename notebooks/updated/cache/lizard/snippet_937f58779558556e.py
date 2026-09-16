def reelect_app(self, request, app):
    app.disconnect()
    endpoints_size = len(app.locator.endpoints)
    for _ in xrange(0, endpoints_size + 1):
        if len(app.locator.endpoints) == 0:
            request.logger.info(
                'giving up on connecting to dist-info hosts, falling back to common pool processing'
                )
            app = yield self.proxy.reelect_app(request, app)
            raise gen.Return(app)
        try:
            locator = Locator(endpoints=app.locator.endpoints)
            request.logger.info('connecting to locator %s', locator.
                endpoints[0])
            yield gen.with_timeout(self.service_connect_timeout, locator.
                connect())
            request.logger.debug('connected to locator %s for %s', locator.
                endpoints[0], app.name)
            app = Service(app.name, locator=locator, timeout=RESOLVE_TIMEOUT)
            yield gen.with_timeout(self.service_connect_timeout, app.connect())
            request.logger.debug('connected to application %s via %s', app.
                name, app.endpoints)
        except gen.TimeoutError:
            request.logger.warning('timed out while connecting to application')
            continue
        except ServiceError as err:
            request.logger.warning('got error while resolving app - %s', err)
            if (err.category in LOCATORCATEGORY and err.code ==
                ESERVICENOTAVAILABLE):
                continue
            else:
                raise err
        finally:
            app.locator.endpoints = app.locator.endpoints[1:]
        raise gen.Return(app)
    raise PluginApplicationError(42, 42, 'could not connect to application')