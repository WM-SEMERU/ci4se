def start_polling(self, reset_webhook=None, timeout=20, fast=True):
    self._prepare_polling()
    loop: asyncio.AbstractEventLoop = self.loop
    try:
        loop.run_until_complete(self._startup_polling())
        loop.create_task(self.dispatcher.start_polling(reset_webhook=
            reset_webhook, timeout=timeout, fast=fast))
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        loop.run_until_complete(self._shutdown_polling())
        log.warning('Goodbye!')