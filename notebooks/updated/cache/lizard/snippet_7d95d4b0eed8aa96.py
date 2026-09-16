def subparsers(self):
    try:
        return self.__subparsers
    except AttributeError:
        parent = super(ArgumentParser, self)
        self.__subparsers = parent.add_subparsers(title='drill down')
        self.__subparsers.metavar = 'COMMAND'
        return self.__subparsers