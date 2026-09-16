def get_branding_ids(self):
    if 'brandingIds' not in self.my_osid_object._my_map:
        return IdList([])
    id_list = []
    for idstr in self.my_osid_object._my_map['brandingIds']:
        id_list.append(Id(idstr))
    return IdList(id_list)