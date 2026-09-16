def run(self, func=None):
    args = self.parser.parse_args()
    if self.__add_vq is not None and self.__config_logging:
        self.__config_logging(args)
    if self.__show_version_func and args.version and callable(self.
        __show_version_func):
        self.__show_version_func(self, args)
    elif args.func is not None:
        args.func(self, args)
    elif func is not None:
        func(self, args)
    else:
        self.parser.print_help()