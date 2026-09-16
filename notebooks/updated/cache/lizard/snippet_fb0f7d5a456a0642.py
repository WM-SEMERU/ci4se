def processModule(module_name):
    r
    Module = sys.modules[module_name]
    MembersTarget = []
    ClassQ = []
    Cls = None
    ClsGroup = None
    ClsGrpMembers = []
    for Member in ModuleMembers[module_name]:
        Underlying = Member.Underlying
        member_name = Member.Config['name']
        member_alias = Member.Config.get('alias', None)
        if ClassQ:
            ClsGroup = ClassQ[-1]
            Cls = ClsGroup.Underlying
            if getattr(Cls, Underlying.__name__, None) is Underlying:
                if isclass(Underlying):
                    ClassQ.append(Underlying.__ec_member__)
                elif not isunderlying(Underlying):
                    continue
                if member_alias:
                    ClsGrpMembers.insert(0, (member_alias, Member))
                ClsGrpMembers.insert(0, (member_name, Member))
                continue
            elif Cls:
                ClsGroup.Members = OrderedDict(ClsGrpMembers)
                ClsGrpMembers = []
                ClassQ.pop()
                Cls = None
                ClsGroup = None
        if isunderlying(Underlying):
            if member_alias:
                MembersTarget.insert(0, (member_alias, Member))
            MembersTarget.insert(0, (member_name, Member))
            if isclass(Underlying):
                ClassQ.append(Underlying.__ec_member__)
    if ClsGroup:
        ClsGroup.Members = OrderedDict(ClsGrpMembers)
    ModuleMembers[module_name] = []
    if not hasattr(Module.__ec_member__, 'Members'):
        Module.__ec_member__.Members = OrderedDict(MembersTarget)