def _on_items_changed(self, change):
    if change['type'] != 'container':
        return
    op = change['operation']
    if op == 'append':
        i = len(change['value']) - 1
        self.adapter.notifyItemInserted(i)
    elif op == 'insert':
        self.adapter.notifyItemInserted(change['index'])
    elif op in ('pop', '__delitem__'):
        self.adapter.notifyItemRemoved(change['index'])
    elif op == '__setitem__':
        self.adapter.notifyItemChanged(change['index'])
    elif op == 'extend':
        n = len(change['items'])
        i = len(change['value']) - n
        self.adapter.notifyItemRangeInserted(i, n)
    elif op in ('remove', 'reverse', 'sort'):
        self.adapter.notifyDataSetChanged()