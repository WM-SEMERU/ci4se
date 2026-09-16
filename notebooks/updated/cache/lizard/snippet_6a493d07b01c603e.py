def search_registry(self, searchterm):
    return self.__search(type_attribute=self.__mispregistrytypes(), value=
        searchterm)