def acctran(tree, character, feature=PARS_STATES):
    ps_feature_down = get_personalized_feature_name(character, BU_PARS_STATES)
    for node in tree.traverse('preorder'):
        if node.is_root():
            node.add_feature(feature, getattr(node, ps_feature_down))
        node_states = getattr(node, feature)
        for child in node.children:
            child_states = getattr(child, ps_feature_down)
            state_intersection = node_states & child_states
            child.add_feature(feature, state_intersection if
                state_intersection else child_states)