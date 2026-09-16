def ref_for_message_type(self, message_type):
    name = self.__normalized_name(message_type)
    if name not in self.__schemas:
        raise KeyError('Message has not been parsed: %s', name)
    return name