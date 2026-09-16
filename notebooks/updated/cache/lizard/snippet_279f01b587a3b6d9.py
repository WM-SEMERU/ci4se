def root_hash(self):
    if self.__root_hash is None:
        self.__root_hash = self.__hasher._hash_fold(self.__hashes
            ) if self.__hashes else self.__hasher.hash_empty()
    return self.__root_hash