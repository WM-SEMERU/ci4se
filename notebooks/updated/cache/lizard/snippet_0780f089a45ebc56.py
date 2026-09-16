def __validInterval(self, start, finish):
    url = self.__getURL(1, start.strftime('%Y-%m-%d'), finish.strftime(
        '%Y-%m-%d'))
    data = self.__readAPI(url)
    if data['total_count'] >= 1000:
        middle = start + (finish - start) / 2
        self.__validInterval(start, middle)
        self.__validInterval(middle, finish)
    else:
        self.__intervals.append([start.strftime('%Y-%m-%d'), finish.
            strftime('%Y-%m-%d')])
        self.__logger.info('New valid interval: ' + start.strftime(
            '%Y-%m-%d') + ' to ' + finish.strftime('%Y-%m-%d'))