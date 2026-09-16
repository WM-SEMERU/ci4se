def createShadowHandlerWithName(self, shadowName, isPersistentSubscribe):
    return deviceShadow.deviceShadow(shadowName, isPersistentSubscribe,
        self._shadowManager)