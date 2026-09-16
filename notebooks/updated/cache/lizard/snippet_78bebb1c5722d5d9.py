def omitted_predictions(self):
    if self.__omitted_predictions is None:
        self.log('loading omitted_predictions')
        self.__load_omitted_predictions()
        self.log('loading omitted_predictions')
    return self.__omitted_predictions