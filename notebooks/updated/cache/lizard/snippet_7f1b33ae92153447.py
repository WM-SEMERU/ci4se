def write(self):
    outfn = self.create_outfilepath(self.fn, self.outsuffix)
    command = ['qvality']
    command.extend(self.qvalityoptions)
    command.extend([self.scores['target']['fn'], self.scores['decoy']['fn'],
        '-o', outfn])
    subprocess.call(command)