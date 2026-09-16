def set_base_prompt(self, pri_prompt_terminator='>', alt_prompt_terminator=
    ']', delay_factor=1):
    log.debug('In set_base_prompt')
    delay_factor = self.select_delay_factor(delay_factor)
    self.clear_buffer()
    self.write_channel(self.RETURN)
    time.sleep(0.5 * delay_factor)
    prompt = self.read_channel()
    prompt = self.normalize_linefeeds(prompt)
    prompt = prompt.split(self.RESPONSE_RETURN)[-1]
    prompt = prompt.strip()
    if not prompt[-1] in (pri_prompt_terminator, alt_prompt_terminator):
        raise ValueError('Router prompt not found: {0}'.format(prompt))
    prompt = re.sub('^HRP_.', '', prompt, flags=re.M)
    prompt = prompt[1:-1]
    prompt = prompt.strip()
    self.base_prompt = prompt
    log.debug('prompt: {0}'.format(self.base_prompt))
    return self.base_prompt