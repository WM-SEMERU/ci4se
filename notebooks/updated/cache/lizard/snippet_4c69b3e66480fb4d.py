def get(self, comp_name):
    try:
        return self.__cache[comp_name]
    except KeyError:
        comp_stub = ComponentStub(self, comp_name, self.__prof)
        self.__cache[comp_name] = comp_stub
        return comp_stub