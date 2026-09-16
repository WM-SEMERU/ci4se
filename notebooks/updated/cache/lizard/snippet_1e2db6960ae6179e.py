def readrows(self):
    reconnecting = True
    while True:
        try:
            for row in self._readrows():
                if reconnecting:
                    print('Successfully monitoring {:s}...'.format(self.
                        _filepath))
                    reconnecting = False
                yield row
        except IOError:
            if self._tail:
                print('Could not open file {:s} Retrying...'.format(self.
                    _filepath))
                reconnecting = True
                time.sleep(5)
                continue
            else:
                break
        if self._tail:
            print('File closed {:s} Retrying...'.format(self._filepath))
            reconnecting = True
            time.sleep(5)
            continue
        else:
            break