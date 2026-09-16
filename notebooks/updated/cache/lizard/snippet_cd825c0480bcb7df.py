def Decorate(cls, class_name, member, parent_member):
    if isinstance(member, property):
        fget = cls.DecorateMethod(class_name, member.fget, parent_member)
        fset = None
        if member.fset:
            fset = cls.DecorateMethod(class_name, member.fset, parent_member)
        fdel = None
        if member.fdel:
            fdel = cls.DecorateMethod(class_name, member.fdel, parent_member)
        return property(fget, fset, fdel, member.__doc__)
    else:
        return cls.DecorateMethod(class_name, member, parent_member)