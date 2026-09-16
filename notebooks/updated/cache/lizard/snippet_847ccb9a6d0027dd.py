def read(self, size=-1):
    if not size:
        return defer.succeed(None)
    remainder = int(self.length) - self.__position
    if size < 0 or size > remainder:
        size = remainder


    class State(object):
        pass
    state = State()
    state.data = self.__buffer
    state.chunk_number = (len(state.data) + self.__position) / self.chunk_size

    def iterate(_=None):
        if len(state.data) < size:
            return self.__chunks.find_one({'files_id': self._id, 'n': state
                .chunk_number}).addCallback(process).addCallback(iterate)
        return defer.succeed(None)

    def process(chunk):
        if not chunk:
            raise CorruptGridFile('TxMongo: no chunk #{0}'.format(state.
                chunk_number))
        if not state.data:
            state.data += chunk['data'][self.__position % self.chunk_size:]
        else:
            state.data += chunk['data']
        state.chunk_number += 1

    def done(_):
        self.__position += size
        to_return = state.data[:size]
        self.__buffer = state.data[size:]
        return to_return
    return iterate().addCallback(done)