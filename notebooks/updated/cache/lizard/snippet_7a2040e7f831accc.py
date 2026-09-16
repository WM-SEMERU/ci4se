def _parse_relationship(self):
    rs_dict = self.data.get('relationships', {})
    for rs_name in self.KNOWN_RELATIONSHIPS:
        if rs_name in rs_dict:
            setattr(self, rs_name, Relationship(rs_name, rs_dict.get(rs_name)))
        else:
            setattr(self, rs_name, NoneRelationshipSingleton)