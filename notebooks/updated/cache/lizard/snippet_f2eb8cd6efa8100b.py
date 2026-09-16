def ParseMultiple(self, stats, knowledge_base):
    user_dict = {}
    for stat in stats:
        sid_str = stat.pathspec.path.split('/', 3)[2]
        if SID_RE.match(sid_str):
            if sid_str not in user_dict:
                user_dict[sid_str] = rdf_client.User(sid=sid_str)
            if stat.registry_data.GetValue():
                reg_key_name = stat.pathspec.Dirname().Basename()
                if reg_key_name in self.key_var_mapping:
                    map_dict = self.key_var_mapping[reg_key_name]
                    reg_key = stat.pathspec.Basename()
                    kb_attr = map_dict.get(reg_key)
                    if kb_attr:
                        value = (artifact_utils.
                            ExpandWindowsEnvironmentVariables(stat.
                            registry_data.GetValue(), knowledge_base))
                        value = (artifact_utils.
                            ExpandWindowsUserEnvironmentVariables(value,
                            knowledge_base, sid=sid_str))
                        user_dict[sid_str].Set(kb_attr, value)
    return itervalues(user_dict)