def has_provenance(self):
    if 'provenanceId' in self.my_osid_object._my_map:
        return bool(self.my_osid_object._my_map['provenanceId'] != '')
    else:
        return bool(self.my_osid_object._my_map['provenanceItemId'] != '')