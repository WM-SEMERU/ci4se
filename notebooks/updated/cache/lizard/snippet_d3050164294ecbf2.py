def get_fragment_generator(self, gp, **kwargs):
    collector = FragmentCollector(self.__host, gp)
    return collector.get_fragment_generator(**kwargs)