def _con(self):


    class Constraints(object):

        def __getitem__(_self, name):
            return self.getConstraint(name)

        def __setitem__(_self, name, value):
            self.getConstraint(name).setDual(value)

        def __iter__(_self):
            return self.getConstraints()
    return Constraints()