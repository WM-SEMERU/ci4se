def get_genus_type(self):
    try:
        genus_type_identifier = Id(self._my_map['genusTypeId']).get_identifier(
            )
        return Type(**types.Genus().get_type_data(genus_type_identifier))
    except:
        return Type(idstr=self._my_map['genusTypeId'])