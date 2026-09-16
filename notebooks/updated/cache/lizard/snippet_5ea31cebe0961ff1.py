def group_items(self, labels):
    import utool as ut
    unique_labels, groups = self.group(labels)
    label_to_group = ut.odict(zip(unique_labels, groups))
    return label_to_group