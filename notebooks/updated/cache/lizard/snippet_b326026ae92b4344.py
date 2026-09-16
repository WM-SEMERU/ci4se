def _check_ep(interface, ep_index, ep_dir, ep_type):
    ep = interface[ep_index]
    return usb.util.endpoint_direction(ep.bEndpointAddress
        ) == ep_dir and usb.util.endpoint_type(ep.bmAttributes) == ep_type