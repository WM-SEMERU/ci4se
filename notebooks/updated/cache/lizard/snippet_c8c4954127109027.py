def fork(self, strictindex, new_value):
    forked_chunk = YAMLChunk(deepcopy(self._ruamelparsed), pointer=self.
        pointer, label=self.label, key_association=copy(self._key_association))
    forked_chunk.contents[self.ruamelindex(strictindex)
        ] = new_value.as_marked_up()
    forked_chunk.strictparsed()[strictindex] = deepcopy(new_value.
        as_marked_up())
    return forked_chunk