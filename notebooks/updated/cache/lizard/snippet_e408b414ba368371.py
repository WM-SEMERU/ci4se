def done(self):
    sys.stdout.write('\x08{0}Done{1}\n'.format(self.meta.color['GREY'],
        self.meta.color['ENDC']))