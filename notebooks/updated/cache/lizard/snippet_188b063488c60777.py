def now(self):
    try:
        if self.now_id:
            return Chart(self.now_id)
        else:
            log.debug('attempted to get current chart, but none was found')
            return
    except AttributeError:
        log.debug(
            'attempted to get current ("now") chart from a chart without a now attribute'
            )
        return None