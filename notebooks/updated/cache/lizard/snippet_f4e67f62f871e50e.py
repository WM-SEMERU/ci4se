async def _cancel(log, **tasks):
    for name, task in tasks.items():
        if not task:
            continue
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
        except Exception:
            log.exception('Unhandled exception from %s after cancel', name)