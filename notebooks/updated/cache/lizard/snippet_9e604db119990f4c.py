def listed(self):
    print('\nPackages in the blacklist:\n')
    for black in self.get_black():
        if black:
            print('{0}{1}{2}'.format(self.meta.color['GREEN'], black, self.
                meta.color['ENDC']))
            self.quit = True
    if self.quit:
        print('')