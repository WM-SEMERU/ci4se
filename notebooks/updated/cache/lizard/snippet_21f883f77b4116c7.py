def mark(self, element):
    logger.debug('Element : {elm}'.format(elm=str(element)))
    if element is not None:
        logger.debug('Mark as not fresh')
        element.freshness = False
    logger.debug(str(self.cache))