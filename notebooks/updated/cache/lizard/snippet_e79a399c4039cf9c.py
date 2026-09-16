def get_branch_length(self, age=None, pos=0):
    if age is None:
        age = self.age
    return self.length * pow(self.branches[pos][0], age)