def shadow(self, new_root, visitor):
    for n in self.walk():
        sn = n.clone(new_root)
        if n.isdir():
            visitor.process_dir(n, sn)
        else:
            visitor.process_file(n, sn)