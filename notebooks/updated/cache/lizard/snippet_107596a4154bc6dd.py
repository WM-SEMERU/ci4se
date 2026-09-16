def get_channel(device, ch_name, channel_dict, loader, resource_dict):
    channel_dict = get_bases(channel_dict, loader)
    r_ids = resource_dict.get('channel_ids', {}).get(ch_name, [])
    ids = r_ids if r_ids else channel_dict.get('ids', {})
    can_select = False if channel_dict.get('can_select') == 'False' else True
    channels = Channels(device, ids, can_select)
    update_component(ch_name, channels, channel_dict)
    return channels