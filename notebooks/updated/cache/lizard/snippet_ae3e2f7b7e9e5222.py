def export_to_file(self, filename):
    instr_json = self.export_struct()
    with open(filename, 'w') as fp:
        json.dump(instr_json, fp, indent=2)