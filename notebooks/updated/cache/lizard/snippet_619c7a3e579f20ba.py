def run(self):
    if not self.scent or len(self.scent.runners) == 0:
        print("Did not find 'scent.py', running nose:")
        return super(ScentSniffer, self).run()
    else:
        print('Using scent:')
        arguments = [sys.argv[0]] + list(self.test_args)
        return self.scent.run(arguments)
    return True