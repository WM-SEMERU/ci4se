def _var(self):


    class Variables(object):

        def __getitem__(_self, name):
            return self.getVariable(name)

        def __setitem__(_self, name, value):
            self.getVariable(name).setValue(value)

        def __iter__(_self):
            return self.getVariables()
    return Variables()