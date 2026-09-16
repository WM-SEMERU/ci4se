def _trans_as_path(self, as_path_list):

    def _swap(n):
        if is_valid_old_asn(n):
            return n
        else:
            return bgp.AS_TRANS
    if self.is_four_octet_as_number_cap_valid():
        return as_path_list, None
    else:
        new_as_path_list = []
        for as_path in as_path_list:
            if isinstance(as_path, set):
                path_set = set()
                for as_num in as_path:
                    path_set.add(_swap(as_num))
                new_as_path_list.append(path_set)
            elif isinstance(as_path, list):
                path_list = list()
                for as_num in as_path:
                    path_list.append(_swap(as_num))
                new_as_path_list.append(path_list)
            else:
                pass
        if as_path_list == new_as_path_list:
            return as_path_list, None
        return new_as_path_list, as_path_list