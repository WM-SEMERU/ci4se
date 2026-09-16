def _config_win32_nameservers(self, nameservers):
    nameservers = str(nameservers)
    split_char = self._determine_split_char(nameservers)
    ns_list = nameservers.split(split_char)
    for ns in ns_list:
        if not ns in self.nameservers:
            self.nameservers.append(ns)