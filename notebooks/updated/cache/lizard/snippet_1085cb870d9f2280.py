def jsonFn(self, comic):
    fn = os.path.join(self.basepath, comic, 'dosage.json')
    fn = os.path.abspath(fn)
    return fn