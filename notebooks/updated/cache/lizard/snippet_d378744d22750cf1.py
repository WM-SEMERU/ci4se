def incomplete_relation_data(configs, required_interfaces):
    complete_ctxts = configs.complete_contexts()
    incomplete_relations = [svc_type for svc_type, interfaces in
        required_interfaces.items() if not set(interfaces).intersection(
        complete_ctxts)]
    return {i: configs.get_incomplete_context_data(required_interfaces[i]) for
        i in incomplete_relations}