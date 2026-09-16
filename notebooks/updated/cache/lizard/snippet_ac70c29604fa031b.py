def train(self, record):
    self.n += 1
    class_attr = self.tree.data.class_attribute_name
    class_value = record[class_attr]
    is_con = self.tree.data.is_continuous_class
    if is_con:
        self._class_cdist += class_value
    else:
        self._class_ddist.add(class_value)
    for an, av in iteritems(record):
        if an == class_attr:
            continue
        self._attr_value_counts[an][av] += 1
        self._attr_value_count_totals[an] += 1
        if is_con:
            self._attr_value_cdist[an][av] += class_value
        else:
            self._attr_class_value_counts[an][av][class_value] += 1
    if self.ready_to_split:
        self.attr_name = self.get_best_splitting_attr()
        self.tree.leaf_count -= 1
        for av in self._attr_value_counts[self.attr_name]:
            self._branches[av] = Node(tree=self.tree)
            self.tree.leaf_count += 1
    if self.attr_name:
        key = record[self.attr_name]
        del record[self.attr_name]
        self._branches[key].train(record)