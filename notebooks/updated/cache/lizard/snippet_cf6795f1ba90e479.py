def delete_alias(self, alias, indices):
    indices = self.conn._validate_indices(indices)
    return self.change_aliases(['remove', index, alias, {}] for index in
        indices)