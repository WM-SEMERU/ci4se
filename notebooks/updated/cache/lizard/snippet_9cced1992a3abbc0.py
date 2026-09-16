def __send_message(self, operation):

    def kill():
        self.__killed = True
        self.__end_session(True)
    client = self.__collection.database.client
    try:
        response = client._run_operation_with_response(operation, self.
            _unpack_response, address=self.__address)
    except OperationFailure:
        kill()
        raise
    except NotMasterError:
        kill()
        raise
    except ConnectionFailure:
        kill()
        raise
    except Exception:
        self.__die()
        raise
    from_command = response.from_command
    reply = response.data
    docs = response.docs
    if from_command:
        cursor = docs[0]['cursor']
        documents = cursor['nextBatch']
        self.__id = cursor['id']
    else:
        documents = docs
        self.__id = reply.cursor_id
    if self.__id == 0:
        kill()
    self.__data = deque(documents)