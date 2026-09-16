def _obj(self):


    class Objectives(object):

        def __getitem__(_self, name):
            return self.getObjective(name)

        def __iter__(_self):
            return self.getObjectives()
    return Objectives()