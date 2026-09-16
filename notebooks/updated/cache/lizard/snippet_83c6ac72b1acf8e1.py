def of(self, klass, name='default'):
    return FactoryBuilder(klass, name, self._definitions, self._faker, self
        ._resolver)