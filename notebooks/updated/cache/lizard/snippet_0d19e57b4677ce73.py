def runPowerNotificationsThread(self):
    pool = NSAutoreleasePool.alloc().init()

    @objc.callbackFor(IOPSNotificationCreateRunLoopSource)
    def on_power_source_notification(context):
        with self._lock:
            for weak_observer in self._weak_observers:
                observer = weak_observer()
                if observer:
                    observer.on_power_source_notification()
    self._source = IOPSNotificationCreateRunLoopSource(
        on_power_source_notification, None)
    CFRunLoopAddSource(NSRunLoop.currentRunLoop().getCFRunLoop(), self.
        _source, kCFRunLoopDefaultMode)
    while not NSThread.currentThread().isCancelled():
        NSRunLoop.currentRunLoop().runMode_beforeDate_(NSDefaultRunLoopMode,
            NSDate.distantFuture())
    del pool