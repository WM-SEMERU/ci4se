def remove_from_cluster(self, name, *args):
    cluster = self.get_cluster(name=name)
    attrs_ = cluster['cluster']
    for a in args:
        del attrs_[a]