def host_key_checking(enable):

    def as_string(b):
        return b and 'True' or 'False'
    with environment_variable('ANSIBLE_HOST_KEY_CHECKING', as_string(enable)):
        previous = ansible.constants.HOST_KEY_CHECKING
        ansible.constants.HOST_KEY_CHECKING = enable
        yield
        ansible.constants.HOST_KEY_CHECKING = previous