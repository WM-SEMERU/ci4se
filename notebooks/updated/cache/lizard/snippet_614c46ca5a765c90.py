def simulation(self, data=None):
    if data:
        return self._session.put(self.__v2() + '/simulation', data=data)
    else:
        return self._session.get(self.__v2() + '/simulation').json()