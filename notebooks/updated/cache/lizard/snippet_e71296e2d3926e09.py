def export_history(self, dirname):
    mods = [(m.__name__, m.__version__) for m in sys.modules.values() if m if
        hasattr(m, '__version__')]
    with open(dirname + '/requirements.txt', 'w') as f:
        for m in mods:
            m = list(m)
            if not isinstance(m[1], str):
                m[1] = m[1].decode('utf-8')
            f.writelines(m[0] + ' == ' + m[1] + '\n')
    with open(dirname + '/TenetoBIDShistory.py', 'w') as f:
        f.writelines('import teneto\n')
        for func, args in self.history:
            f.writelines(func + '(**' + str(args) + ')\n')
    with open(dirname + '/tenetoinfo.json', 'w') as f:
        json.dump(self.tenetoinfo, f)