def create_l2vpnflowspec_actions(actions=None):
    from ryu.services.protocols.bgp.api.prefix import FLOWSPEC_ACTION_TRAFFIC_RATE, FLOWSPEC_ACTION_TRAFFIC_ACTION, FLOWSPEC_ACTION_REDIRECT, FLOWSPEC_ACTION_TRAFFIC_MARKING, FLOWSPEC_ACTION_VLAN, FLOWSPEC_ACTION_TPID
    action_types = {FLOWSPEC_ACTION_TRAFFIC_RATE:
        BGPFlowSpecTrafficRateCommunity, FLOWSPEC_ACTION_TRAFFIC_ACTION:
        BGPFlowSpecTrafficActionCommunity, FLOWSPEC_ACTION_REDIRECT:
        BGPFlowSpecRedirectCommunity, FLOWSPEC_ACTION_TRAFFIC_MARKING:
        BGPFlowSpecTrafficMarkingCommunity, FLOWSPEC_ACTION_VLAN:
        BGPFlowSpecVlanActionCommunity, FLOWSPEC_ACTION_TPID:
        BGPFlowSpecTPIDActionCommunity}
    return _create_actions(actions, action_types)