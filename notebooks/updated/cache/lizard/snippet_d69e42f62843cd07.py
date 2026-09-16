def set_public_lan(lan_id):
    conn = get_conn()
    datacenter_id = get_datacenter_id()
    try:
        lan = conn.get_lan(datacenter_id=datacenter_id, lan_id=lan_id)
        if not lan['properties']['public']:
            conn.update_lan(datacenter_id=datacenter_id, lan_id=lan_id,
                public=True)
        return lan['id']
    except Exception:
        lan = conn.create_lan(datacenter_id, LAN(public=True, name=
            'Public LAN'))
        return lan['id']