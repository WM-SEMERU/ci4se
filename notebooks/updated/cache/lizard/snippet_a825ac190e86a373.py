async def with_exception(self, subprocess, *matchers):

    def _callback(event, matcher):
        raise RoutineException(matcher, event)
    return await self.with_callback(subprocess, _callback, *matchers)