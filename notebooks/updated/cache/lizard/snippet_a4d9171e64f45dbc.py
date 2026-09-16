def _remove(self, xer, primary):
    if xer in primary:
        notifier = primary.pop(xer)
        notifier.shutdown()