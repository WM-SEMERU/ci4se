def add_to_parser(self, parser):
    setts = self.settings

    def sorter(x):
        return setts[x].section, setts[x].order
    for k in sorted(setts, key=sorter):
        setts[k].add_argument(parser)
    return parser