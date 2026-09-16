def send_vdp_assoc(self, vsiid=None, mgrid=None, typeid=None, typeid_ver=
    None, vsiid_frmt=vdp_const.VDP_VSIFRMT_UUID, filter_frmt=vdp_const.
    VDP_FILTER_GIDMACVID, gid=0, mac='', vlan=0, oui_id='', oui_data='',
    sw_resp=False):
    if sw_resp and filter_frmt == vdp_const.VDP_FILTER_GIDMACVID:
        reply = self.send_vdp_query_msg('assoc', mgrid, typeid, typeid_ver,
            vsiid_frmt, vsiid, filter_frmt, gid, mac, vlan, oui_id, oui_data)
        vlan_resp, fail_reason = self.get_vlan_from_query_reply(reply,
            vsiid, mac)
        if vlan_resp != constants.INVALID_VLAN:
            return vlan_resp, fail_reason
    reply = self.send_vdp_msg('assoc', mgrid, typeid, typeid_ver,
        vsiid_frmt, vsiid, filter_frmt, gid, mac, vlan, oui_id, oui_data,
        sw_resp)
    if sw_resp:
        vlan, fail_reason = self.get_vlan_from_associate_reply(reply, vsiid,
            mac)
        return vlan, fail_reason
    return None, None