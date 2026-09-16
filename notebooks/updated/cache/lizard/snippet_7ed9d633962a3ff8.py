def delete_account(self):
    if self.id_type == IdentityTypes.adobeID:
        raise ArgumentError('You cannot delete an Adobe ID account.')
    self.append(removeFromDomain={})
    return None