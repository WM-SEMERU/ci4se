def show_version(a_device):
    remote_conn = ConnectHandler(**a_device)
    print()
    print('#' * 80)
    print(remote_conn.send_command_expect('show version'))
    print('#' * 80)
    print()