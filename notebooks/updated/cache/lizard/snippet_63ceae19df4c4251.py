def structures(self):
    hstructs = [Structure.from_dict(s['input_structure']) for s in self.
        history if 'input_structure' in s]
    return hstructs + [self.final_structure]