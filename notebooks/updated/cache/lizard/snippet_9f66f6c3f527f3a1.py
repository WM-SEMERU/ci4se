def parse_ireturnvalue(self, tup_tree):
    self.check_node(tup_tree, 'IRETURNVALUE')
    values = self.list_of_same(tup_tree, ('CLASSNAME', 'INSTANCENAME',
        'VALUE', 'VALUE.OBJECTWITHPATH', 'VALUE.OBJECTWITHLOCALPATH',
        'VALUE.OBJECT', 'OBJECTPATH', 'QUALIFIER.DECLARATION',
        'VALUE.ARRAY', 'VALUE.REFERENCE', 'CLASS', 'INSTANCE',
        'INSTANCEPATH', 'VALUE.NAMEDINSTANCE', 'VALUE.INSTANCEWITHPATH'))
    return name(tup_tree), attrs(tup_tree), values