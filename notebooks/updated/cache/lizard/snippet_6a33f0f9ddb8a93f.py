def omitted_parcov(self):
    if self.__omitted_parcov is None:
        self.log('loading omitted_parcov')
        self.__load_omitted_parcov()
        self.log('loading omitted_parcov')
    return self.__omitted_parcov