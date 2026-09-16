def logical_switches(self):
    if not self.__logical_switches:
        self.__logical_switches = LogicalSwitches(self.__connection)
    return self.__logical_switches