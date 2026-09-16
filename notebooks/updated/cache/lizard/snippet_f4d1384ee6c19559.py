def _print_dict_files(self, case, target):
    if case in self.live and target in self.live[case]:
        lines = []
        data = self.live[case][target]
        skeys = list(sorted(data.keys()))
        for key in skeys:
            props = ', '.join(sorted(data[key].keys()))
            lines.append("'{}': {}".format(key, props))
        return '\n'.join(lines)
    else:
        msg.err("Can't find the result set {} in {}".format(target, case))