def get_outputs_filtered(self, owner, spent=None):
    outputs = self.fastquery.get_outputs_by_public_key(owner)
    if spent is None:
        return outputs
    elif spent is True:
        return self.fastquery.filter_unspent_outputs(outputs)
    elif spent is False:
        return self.fastquery.filter_spent_outputs(outputs)