def str_to_datetime(self, format='%Y-%m-%dT%H:%M:%S%ZP'):
    if self.dtype != str:
        raise TypeError('str_to_datetime expects SArray of str as input SArray'
            )
    with cython_context():
        return SArray(_proxy=self.__proxy__.str_to_datetime(format))