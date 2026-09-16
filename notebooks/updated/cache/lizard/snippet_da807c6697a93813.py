def split_interface(intf_name):
    head = intf_name.rstrip('/\\0123456789. ')
    tail = intf_name[len(head):].lstrip()
    return head, tail