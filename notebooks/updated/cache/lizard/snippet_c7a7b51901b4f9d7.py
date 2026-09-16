def _exc_middleware_factory(app):

    @web.middleware
    async def middleware(request, handler):
        try:
            return await handler(request)
        except Exception as exc:
            for cls in type(exc).mro():
                if cls in app._error_handlers:
                    request.exception = exc
                    response = await app._error_handlers[cls](request)
                    return response
            raise
    return middleware