def find_out_member_access_type(self, member):
    assert member.parent is self
    if not member.cache.access_type:
        if member in self.public_members:
            access_type = ACCESS_TYPES.PUBLIC
        elif member in self.protected_members:
            access_type = ACCESS_TYPES.PROTECTED
        elif member in self.private_members:
            access_type = ACCESS_TYPES.PRIVATE
        else:
            raise RuntimeError(
                'Unable to find member within internal members list.')
        member.cache.access_type = access_type
        return access_type
    else:
        return member.cache.access_type