def children(self):
    for child in self.data.get('children', []):
        if osp.exists(osp.join(self.path, child, YAML_REPORT_FILE)):
            yield child, self.__class__(osp.join(self.path, child))