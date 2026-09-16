def process_children(self, node, path, level, parent=None):
    data_parent = parent if parent else node
    chs = node.i_children
    for ch in chs:
        if ch.keyword in ['choice', 'case']:
            self.process_children(ch, path, level, node)
            continue
        p = path + '/' + self.qname(ch)
        tmpl = self.xsl_template(p)
        ct = self.xsl_calltemplate(ch.keyword, tmpl)
        self.xsl_withparam('level', '%d' % level, ct)
        if (data_parent.i_module is None or ch.i_module.i_modulename !=
            data_parent.i_module.i_modulename):
            self.xsl_withparam('nsid', ch.i_module.i_modulename + ':', ct)
        if ch.keyword in ['leaf', 'leaf-list']:
            self.type_param(ch, ct)
        elif ch.keyword != 'anyxml':
            offset = 2 if ch.keyword == 'list' else 1
            self.process_children(ch, p, level + offset)