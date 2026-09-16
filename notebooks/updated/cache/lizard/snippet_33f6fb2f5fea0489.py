def add_predicate(self, pred_obj):
    pred_id = pred_obj.get_id()
    if not pred_id in self.idx:
        pred_node = pred_obj.get_node()
        self.node.append(pred_node)
        self.idx[pred_id] = pred_node
    else:
        print('Error: trying to add new element, but id has already been given'
            )