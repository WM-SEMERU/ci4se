def stop(self):
    if self._state != Bundle.ACTIVE:
        return
    exception = None
    with self._lock:
        previous_state = self._state
        self._state = Bundle.STOPPING
        self._fire_bundle_event(BundleEvent.STOPPING)
        stopper = self.__get_activator_method('stop')
        if stopper is not None:
            try:
                stopper(self.__context)
            except (FrameworkException, BundleException) as ex:
                self._state = previous_state
                _logger.exception('Pelix error raised by %s while stopping',
                    self.__name)
                exception = ex
            except Exception as ex:
                _logger.exception('Error raised by %s while stopping', self
                    .__name)
                exception = BundleException(ex)
        self.__framework._hide_bundle_services(self)
        self._fire_bundle_event(BundleEvent.STOPPING_PRECLEAN)
        self.__unregister_services()
        self.__framework._unget_used_services(self)
        self._state = Bundle.RESOLVED
        self._fire_bundle_event(BundleEvent.STOPPED)
    if exception is not None:
        raise exception