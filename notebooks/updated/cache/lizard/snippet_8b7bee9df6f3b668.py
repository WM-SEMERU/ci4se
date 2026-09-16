def commit(self, confirm=False, confirm_delay=None, comment='', label='',
    delay_factor=1):
    delay_factor = self.select_delay_factor(delay_factor)
    if confirm and not confirm_delay:
        raise ValueError('Invalid arguments supplied to XR commit')
    if confirm_delay and not confirm:
        raise ValueError('Invalid arguments supplied to XR commit')
    if comment and confirm:
        raise ValueError('Invalid arguments supplied to XR commit')
    if comment:
        if '"' in comment:
            raise ValueError('Invalid comment contains double quote')
        comment = '"{0}"'.format(comment)
    label = text_type(label)
    error_marker = 'Failed to'
    alt_error_marker = 'One or more commits have occurred from other'
    if label:
        if comment:
            command_string = 'commit label {} comment {}'.format(label, comment
                )
        elif confirm:
            command_string = 'commit label {} confirmed {}'.format(label,
                text_type(confirm_delay))
        else:
            command_string = 'commit label {}'.format(label)
    elif confirm:
        command_string = 'commit confirmed {}'.format(text_type(confirm_delay))
    elif comment:
        command_string = 'commit comment {}'.format(comment)
    else:
        command_string = 'commit'
    output = self.config_mode()
    output += self.send_command_expect(command_string, strip_prompt=False,
        strip_command=False, delay_factor=delay_factor)
    if error_marker in output:
        raise ValueError('Commit failed with the following errors:\n\n{0}'.
            format(output))
    if alt_error_marker in output:
        output += self.send_command_timing('no', strip_prompt=False,
            strip_command=False, delay_factor=delay_factor)
        raise ValueError('Commit failed with the following errors:\n\n{}'.
            format(output))
    return output