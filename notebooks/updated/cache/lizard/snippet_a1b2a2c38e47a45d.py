def collation(self, collation):
    self.__check_okay_to_chain()
    self.__collation = validate_collation_or_none(collation)
    return self