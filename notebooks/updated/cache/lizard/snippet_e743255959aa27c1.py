async def stop(self):
    await self.__receiver.stop()
    await self.__sender.stop()
    self.__stopped = True