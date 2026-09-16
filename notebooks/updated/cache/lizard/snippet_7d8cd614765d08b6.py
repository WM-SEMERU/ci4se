def microsoft(self, key, x86=False):
    node64 = '' if self.pi.current_is_x86() or x86 else 'Wow6432Node'
    return os.path.join('Software', node64, 'Microsoft', key)