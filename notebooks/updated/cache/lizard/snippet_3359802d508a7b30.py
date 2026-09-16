def _fix_outgoing(self, son, collection):
    for manipulator in reversed(self.__outgoing_manipulators):
        son = manipulator.transform_outgoing(son, collection)
    for manipulator in reversed(self.__outgoing_copying_manipulators):
        son = manipulator.transform_outgoing(son, collection)
    return son