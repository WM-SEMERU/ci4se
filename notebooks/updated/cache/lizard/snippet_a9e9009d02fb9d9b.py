def ALL(self):
    if not self.sas.batch:
        for i in self._names:
            if i.upper() != 'LOG':
                x = self.__getattr__(i)
                if isinstance(x, pd.DataFrame):
                    if self.sas.sascfg.display.lower() == 'zeppelin':
                        print('%text ' + i + '\n' + str(x) + '\n')
                    else:
                        self.sas.DISPLAY(x)
    else:
        ret = []
        for i in self._names:
            if i.upper() != 'LOG':
                ret.append(self.__getattr__(i))
        return ret